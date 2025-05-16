#!/usr/bin/env python3

import geopandas as gpd  # For vector data handling
import rasterio  # For raster data handling
from rasterio.mask import mask  # For masking raster data with vector geometries
import numpy as np  # For numerical operations
import os  # For file path operations
from shapely.geometry import mapping  # For geometry operations

def validate_file_path(prompt: str, file_types: list) -> str:
    while True:
        file_path = input(prompt)
        
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            continue
            
        # Check file extension
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in file_types:
            print(f"Error: File must be one of these types: {', '.join(file_types)}")
            continue
            
        return file_path

def get_raster_metadata(raster_path: str) -> dict:
    """
    Display metadata information for a raster file
    
    Args:
        raster_path (str): Path to the raster file
        
    Returns:
        dict: Key metadata information
    """
    try:
        with rasterio.open(raster_path) as src:
            metadata = {
                'driver': src.driver,
                'crs': src.crs,
                'width': src.width,
                'height': src.height,
                'bounds': src.bounds,
                'count': src.count,  # number of bands
                'dtype': src.dtypes[0]
            }
            
            # Print metadata for user reference
            print("\nRaster File Metadata:")
            print(f"Driver: {metadata['driver']}")
            print(f"CRS: {metadata['crs']}")
            print(f"Dimensions: {metadata['width']} x {metadata['height']}")
            print(f"Bounds: {metadata['bounds']}")
            print(f"Number of bands: {metadata['count']}")
            print(f"Data type: {metadata['dtype']}")
            
            return metadata
            
    except Exception as e:
        print(f"Error reading raster metadata: {str(e)}")
        return None

def get_vector_metadata(vector_path: str) -> dict:
    """
    Display metadata information for a vector file
    
    Args:
        vector_path (str): Path to the vector file
        
    Returns:
        dict: Key metadata information
    """
    try:
        # Read the vector file using geopandas
        gdf = gpd.read_file(vector_path)
        
        # Extract key metadata
        metadata = {
            'crs': gdf.crs,
            'geometry_type': gdf.geometry.geom_type.unique().tolist(),
            'feature_count': len(gdf),
            'bounds': gdf.total_bounds.tolist(),
            'columns': gdf.columns.tolist()
        }
        
        # Print metadata for user reference
        print("\nVector File Metadata:")
        print(f"CRS: {metadata['crs']}")
        print(f"Geometry Types: {metadata['geometry_type']}")
        print(f"Number of Features: {metadata['feature_count']}")
        print(f"Bounds (minx, miny, maxx, maxy): {metadata['bounds']}")
        print(f"Available Columns: {metadata['columns']}")
        
        return metadata
        
    except Exception as e:
        print(f"Error reading vector metadata: {str(e)}")
        return None

def process_vector_data(vector_path: str) -> float:
    """
    Process vector data and calculate statistics
    
    Args:
        vector_path (str): Path to the vector file
        
    Returns:
        float: Average of coordinate values
    """
    try:
        # Read the vector file
        gdf = gpd.read_file(vector_path)
        
        # Extract coordinates from the geometry
        coordinates = []
        for geom in gdf.geometry:
            if geom.geom_type == 'Polygon':
                # Extract coordinates from polygon exterior
                coords = list(geom.exterior.coords)
                coordinates.extend([x for coord in coords for x in coord])
                
        # Calculate average of all coordinate values
        if coordinates:
            average = sum(coordinates) / len(coordinates)
            print(f"\nAverage of all coordinate values: {average}")
            return average
        else:
            print("No coordinates found in the vector file")
            return 0.0
            
    except Exception as e:
        print(f"Error processing vector data: {str(e)}")
        return 0.0

def calculate_zonal_statistics(raster_path: str, vector_path: str, band_index: int = 1) -> float:
    """
    Calculate zonal statistics for raster values within vector polygons
    
    Args:
        raster_path (str): Path to the raster file
        vector_path (str): Path to the vector file
        band_index (int): Index of the raster band to process (1-based)
        
    Returns:
        float: Average value within the polygon
    """
    try:
        # Read the vector file
        gdf = gpd.read_file(vector_path)
        
        # Ensure the vector CRS matches the raster
        with rasterio.open(raster_path) as src:
            if gdf.crs != src.crs:
                gdf = gdf.to_crs(src.crs)
            
            # Get geometries in the format required by rasterio
            geometries = [mapping(geom) for geom in gdf.geometry]
            
            # Mask the raster with vector geometries
            out_image, out_transform = mask(src, geometries, crop=True, band_index=band_index)
            
            # Calculate statistics
            masked_data = np.ma.masked_array(out_image, mask=out_image == src.nodata)
            average = float(np.ma.mean(masked_data))
            
            print(f"\nZonal Statistics:")
            print(f"Average value within polygon(s): {average}")
            
            return average
            
    except Exception as e:
        print(f"Error calculating zonal statistics: {str(e)}")
        return 0.0

def main():
    # Get file paths
    print("\n=== Select Input Files ===")
    vector_path = validate_file_path(
        "Enter the path to the vector file (GeoJSON): ",
        ['.geojson']
    )
    
    raster_path = validate_file_path(
        "Enter the path to the raster file (GeoTIFF): ",
        ['.tif', '.tiff']
    )
    
    # Get metadata for both files
    vector_metadata = get_vector_metadata(vector_path)
    raster_metadata = get_raster_metadata(raster_path)
    
    if vector_metadata is None or raster_metadata is None:
        return
    
    # Process vector data
    print("\n=== Processing Vector Data ===")
    vector_average = process_vector_data(vector_path)
    
    # Calculate zonal statistics
    print("\n=== Calculating Zonal Statistics ===")
    zonal_average = calculate_zonal_statistics(raster_path, vector_path)
    
    # Print final results
    print("\n=== Final Results ===")
    print(f"Vector coordinate average: {vector_average}")
    print(f"Raster zonal average: {zonal_average}")

if __name__ == "__main__":
    main()
