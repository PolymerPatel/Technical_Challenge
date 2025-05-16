#!/usr/bin/env python3

import geopandas as gpd  # For vector data handling
import rasterio  # For raster data handling
from rasterio.mask import mask  # For masking raster data with vector geometries
import numpy as np  # For numerical operations
import os  # For file path operations
from shapely.geometry import mapping  # For geometry operations

def get_file_path(prompt, file_types=None):
    while True:
        file_path = input(prompt)
        
        if file_path.lower() == 'q':
            print("Exiting program.")
            sys.exit()
            
        path = Path(file_path)
        
        if not path.exists():
            print(f"Error: File '{file_path}' does not exist.")
            continue
            
        if file_types and path.suffix.lower() not in file_types:
            print(f"Error: File must be one of these types: {', '.join(file_types)}")
            continue
            
        return file_path

def explore_raster_metadata(raster_path):
    try:
        with rasterio.open(raster_path) as src:
            metadata = {
                "driver": src.driver,
                "crs": src.crs,
                "transform": src.transform,
                "shape": src.shape,
                "width": src.width,
                "height": src.height,
                "bounds": src.bounds,
                "count": src.count,
                "nodata": src.nodata,
                "dtype": src.dtypes[0]
            }

            print("\n=== Raster Metadata ===")
            print(f"Driver: {metadata['driver']}")
            print(f"CRS: {metadata['crs']}")
            print(f"Transform: {metadata['transform']}")
            print(f"Shape (rows, cols): {metadata['shape']}")
            print(f"Width x Height: {metadata['width']} x {metadata['height']}")
            print(f"Bounds: {metadata['bounds']}")
            print(f"Count (bands): {metadata['count']}")
            print(f"Nodata value: {metadata['nodata']}")
            print(f"Data type: {metadata['dtype']}")
            
            return metadata   
    except Exception as e:
        print(f"Error reading raster metadata: {e}")
        return None

def explore_vector_metadata(vector_path):
    try:
        gdf = gpd.read_file(vector_path)

        metadata = {
            "crs": gdf.crs,
            "geometry_type": gdf.geometry.type.unique().tolist(),
            "feature_count": len(gdf),
            "bounds": gdf.total_bounds.tolist(),
            "columns": gdf.columns.tolist()
        }

        print("\n=== Vector Metadata ===")
        print(f"CRS: {metadata['crs']}")
        print(f"Geometry type(s): {metadata['geometry_type']}")
        print(f"Feature count: {metadata['feature_count']}")
        print(f"Bounds (minx, miny, maxx, maxy): {metadata['bounds']}")
        print(f"Attribute columns: {metadata['columns']}")
        
        return metadata
        
    except Exception as e:
        print(f"Error reading vector metadata: {e}")
        return None

def compute_average_from_vector(raster_path, vector_path, band_index=1, visualize=False):
    start_time = time.time()
    
    try:
        with rasterio.open(raster_path) as src:
            if band_index < 1 or band_index > src.count:
                print(f"Error: Band index {band_index} is out of range. Available bands: 1-{src.count}")
                return None, 0, None

            gdf = gpd.read_file(vector_path)
            
            if not all(geom.geom_type in ['Polygon', 'MultiPolygon'] for geom in gdf.geometry):
                print("Error: Vector file must contain polygon geometries only.")
                return None, 0, None
                
            if gdf.crs is not None and src.crs is not None and gdf.crs != src.crs:
                print(f"Reprojecting vector from {gdf.crs} to {src.crs}")
                gdf = gdf.to_crs(src.crs)
            
            raster_bounds = gpd.GeoDataFrame(
                geometry=[gpd.box(*src.bounds)], 
                crs=src.crs
            )
            if not gdf.intersects(raster_bounds.geometry[0]).any():
                print("Warning: Vector polygon does not intersect with raster bounds.")
                return None, 0, None

            geoms = [mapping(geom) for geom in gdf.geometry]
            masked_data, out_transform = mask(src, geoms, crop=True, nodata=src.nodata)
            
            band_index_0 = band_index - 1
            masked_band = masked_data[band_index_0]
            
            if src.nodata is not None:
                valid_pixels = masked_band[masked_band != src.nodata]
            else:
                valid_pixels = masked_band
            
            # Calculate average
            if len(valid_pixels) > 0:
                average = np.mean(valid_pixels)
                pixel_count = len(valid_pixels)
                
                elapsed_time = time.time() - start_time
                print(f"Processing completed in {elapsed_time:.2f} seconds")
                
                return average, pixel_count, masked_data
            else:
                print("No valid pixels found within polygon boundaries.")
                return None, 0, None
                
    except Exception as e:
        print(f"Error computing average: {e}")
        return None, 0, None
#debugging
def main():

    raster_extensions = ['.tif', '.tiff', '.geotiff']
    raster_path = get_file_path(
        "Enter path to raster file (GeoTIFF) or 'q' to quit: ",
        raster_extensions
)
    
    # Explore raster metadata
    raster_metadata = explore_raster_metadata(raster_path)
    
    # Get vector file path
    vector_extensions = ['.geojson', '.json', '.shp', '.kml']
    vector_path = get_file_path(
        "Enter path to vector polygon file (GeoJSON, Shapefile, KML) or 'q' to quit: ",
        vector_extensions
    )
    
    # Explore vector metadata
    vector_metadata = explore_vector_metadata(vector_path)
  
    # Compute and display the result
    average, pixel_count, masked_data = compute_average_from_vector(
        raster_path, vector_path, band_index, visualize
    )
    
    if average is not None:
        print(f"Results:")
        print(f"Average value of {pixel_count} cells within polygon: {average:.6f}")
        
        # Calculate additional statistics
        if masked_data is not None:
            band_data = masked_data[band_index - 1]
            if raster_metadata and raster_metadata["nodata"] is not None:
                valid_data = band_data[band_data != raster_metadata["nodata"]]
            else:
                valid_data = band_data.flatten()
    else:
        print("Could not calculate average. No valid pixels found within polygon.")
    
    print("Done!")


if __name__ == "__main__":
    main()
