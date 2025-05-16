import geopandas as gpd
from rasterio.mask import mask
from shapely.geometry import mapping
import numpy as np

###Create a program that asks the user to enter a file path to an arbitrary raster (GEOTIFF)
###And create a program that ask the user to enter a path to a vector polygon GEOJSON file
### It will return the total sum and divide it by the length of the list


nums_list_JSON = [] # list()
nums_list_shp = []
nums_list_bounds = []

UI_polygon_filepath = input("Enter a GeoTIFF file path, shp, or JSON: ")

#pass in two parameters in function
def filepath(UI_polygon_filepath):
    if UI_polygon_filepath == "JSON":
        in_geojson = r'/Users/Owner1/Desktop/Practical coding/polygon.geojson'
        gdf = gpd.read_file('in_geojson')
        gdf = gdf.to_crs(src.crs)
        #nums_list_JSON.append((vector_polygon))

        masked_data = masked[0]  # first band
        valid_pixels = masked_data[masked_data != src.nodata]
        average = np.mean(valid_pixels)

        ###Task 2: Exploring raster file data and metadata.
        ###Note what transformaitons are required during the task
        geom = [mapping(gdf.geometry[0])]
        masked, out_transform = mask(src, geom, crop=True)

        with rasterio.open(r'/Users/Owner1/Desktop/Practical coding/polygon.geojson', 'w',
                            print("Driver:", src.driver),
                            print("CRS:", src.crs),
                            print("Transform:", src.transform),
                            print("Shape:", src.shape),
                            print("Count (bands):", src.count),
                            ) as dst:
                        dst.write(data)
                        ds.meta
                        ds.name
                        ds.count
                        ds.shape
        break

    user_input = input("Enter a file path, shp, or q to quit: ")

    elif user_input == "shp":
        in_shp = r'/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp'
        gdf = gpd.read_file('in_shp')
        gdf = gdf.to_crs(src.crs)
        #nums_list_shp.append(vector_in_shp)

        masked_data = masked[0]  # first band
        valid_pixels = masked_data[masked_data != src.nodata]
        average = np.mean(valid_pixels)

        #Task 2 continued

        geom = [mapping(gdf.geometry[0])]
        masked, out_transform = mask(src, geom, crop=True)

        with rasterio.open(r'/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp', 'w',
                            print("Driver:", src.driver),
                            print("CRS:", src.crs),
                            print("Transform:", src.transform),
                            print("Shape:", src.shape),
                            print("Count (bands):", src.count),
                            ) as dst:
                        dst.write(data)
                        ds.meta
                        ds.name
                        ds.count
                        ds.shape
        break

        user_input_2 = input("Enter a file path, or q to quit: ")


    #arbitrary raster
    else user_input_2 != q:
        in_arbitrary_raster = r'UI_polygon_filepath'
        ds_3 = rasterio.open(in_arbitrary_raster)
        data = ds_3.read()

        raster_mean_function = sum(nums_list_bounds) / len(nums_list_bounds)
        return raster_mean_function

      with rasterio.open(r'UI_polygon_filepath', 'w',
                            print("Driver:", src.driver),
                            print("CRS:", src.crs),
                            print("Transform:", src.transform),
                            print("Shape:", src.shape),
                            print("Count (bands):", src.count),
                            ) as dst:
                        dst.write(data)
                        ds.meta
                        ds.name
                        ds.count
                        ds.shape
        break



def filepath(read_geojson)
def filepath(read_shp)
def filepath(read_TIFF)

print(JSON_mean_function)
print(shp_mean_function)
print(raster_mean_function)