import geopandas as gpd
from rasterio.mask import mask
from shapely.geometry import mapping
import numpy as np

"""
Use of chatgpt or claude.ai is only once the code is ready to submit for review, polishing the code, and landing the code.
Only use ChatGPT, Claude, or cursor if I struggle with something such as "How do I ask for user input in Python?"

It's only for learning and not for writing code.
When I am stuck on a problem, use AI. However, I understand that I am responsible for understanding my code.

"""

raster_path = input("Enter a GeoTIFF file path, shp, or JSON: ")

#pass in two parameters in function
def compute_average_from_vector(raster_path, vector_path):
    in_geojson = r'/Users/Owner1/Desktop/Practical coding/polygon.geojson'
    gdf = gpd.read_file('in_geojson')
    gdf = gdf.to_crs(src.crs)

    masked_data = masked[0]  # first band
    valid_pixels = masked_data[masked_data != src.nodata]
    average = np.mean(valid_pixels)

    geom = [mapping(gdf.geometry[0])]
    masked, out_transform = mask(src, geom, crop=True)

    with rasterio.open(r'/Users/Owner1/Desktop/Practical coding/polygon.geojson') as src:
                        print("Driver:", src.driver),
                        print("CRS:", src.crs),
                        print("Transform:", src.transform),
                        print("Shape:", src.shape),
                        print("Count (bands):", src.count),
                        print("Metadata:", src.meta)
    return average

user_input = input("Enter a file path, shp, or q to quit: ")

def compute_average_from_vector_2(raster_path, vector_path):
    in_shp = r'/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp'
    gdf = gpd.read_file('in_shp')
    gdf = gdf.to_crs(src.crs)

    masked_data = masked[0]  # first band
    valid_pixels = masked_data[masked_data != src.nodata]
    average = np.mean(valid_pixels)

    geom = [mapping(gdf.geometry[0])]
    masked, out_transform = mask(src, geom, crop=True)

    with rasterio.open(r'/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp') as src:
                        print("Driver:", src.driver),
                        print("CRS:", src.crs),
                        print("Transform:", src.transform),
                        print("Shape:", src.shape),
                        print("Count (bands):", src.count),
                        print("Metadata:", src.meta)
    return average

    user_input_2 = input("Enter a file path, or q to quit: ")

    #arbitrary raster
def compute_average_from_vector_3(raster_path, vector_path):
    in_arbitrary_raster = r'UI_polygon_filepath'
    ds_3 = rasterio.open(in_arbitrary_raster)
    data = ds_3.read()

    masked_data = masked[0]  # first band
    valid_pixels = masked_data[masked_data != src.nodata]
    average = np.mean(valid_pixels)

    with rasterio.open(r'UI_polygon_filepath') as src:
                        print("Driver:", src.driver),
                        print("CRS:", src.crs),
                        print("Transform:", src.transform),
                        print("Shape:", src.shape),
                        print("Count (bands):", src.count),
                        print("Metadata:", src.meta)
    return average

compute_average_from_vector(raster_path)
compute_average_from_vector_2()
compute_average_from_vector_3()
