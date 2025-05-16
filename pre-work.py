import geopandas as gpd
import matplotlib
import dask
import rasterio
import fiona




"""
Challenge: Create a program that asks the user to enter a file path to an arbitrary raster (GEOTIFF)
And create a program that ask the user to enter a path to a vector polygon GEOJSON file
It will return the total sum and divide it by the length of the list

"""

nums_list_JSON = [] # list()
nums_list_shp = []
nums_list_bounds = []

UI_polygon_filepath = input("Enter a GeoTIFF file path, shp, or JSON: ")

#pass in two parameters in function
def filepath(UI_polygon_filepath):
    while UI_polygon_filepath == "JSON":
        in_geojson = r'/Users/Owner1/Desktop/Practical coding/polygon.geojson'
        read_geojson = gpd.read_file(in_geojson)
        vector_polygon = read_geojson.head()
        nums_list_JSON.append((vector_polygon))

        #sum function, more concise
        print(total)

        JSON_mean_function = sum(nums_list_JSON) / len(nums_list_JSON)
        return JSON_mean_function
        print(JSON_mean_function)


        ###Task 2
        ds = rasterio.open(in_geojson)
        data = ds.read()

        ###Exploring raster file data and metadata
        ###Note what transformaitons are required during the task

        #Approach 1

        #Find cell width and height
        ds.meta
        #file name
        ds.name
        #bands in file
        ds.count
        ds.shape
        ds.width
        ds.height
        # should return 'GTiff'
        ds.driver
        ds.crs
        ds.descriptions
        data.size
        dtype('uint8')
        data.min()
        data.min()

        with rasterio.open(r'/Users/Owner1/Desktop/Practical coding/polygon.geojson', 'w',
                            driver = ds.driver,
                            height = ds.height,
                            width = ds.width,
                            count = ds.count,
                            crs = ds.crs,
                            transform = ds.transform,
                            dtype = data.dtype,
                            ) as dst:
                        dst.write(data)

        user_input = input("Enter a file path, shp, or q to quit: ")

    while user_input == "shp":
        in_shp = r'/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp'
        read_shp = gpd.read_file(in_shp)
        vector_in_shp = read_shp.head()
        nums_list_shp.append(vector_in_shp)

        print(total)

        shp_mean_function = sum(nums_list_shp) / len(nums_list_shp)
        return shp_mean_function
        print(shp_mean_function)


        #Task 2 continued
        #Approach 2

        with fiona.open('/Users/Owner1/Desktop/Practical coding/drive-download-20250512T201856Z-001/star.shp') as shapefile:
            for feature in shapefile:
                shapes = [feature['geometry']]

        #with rasterio.open()
        #get meta data through python dictionary

        user_input_2 = input("Enter a file path, or q to quit: ")


    #arbitrary raster
    while user_input_2 != q:
        in_arbitrary_raster = r'UI_polygon_filepath'
        ds_3 = rasterio.open(in_arbitrary_raster)
        data = ds_3.read()


        #in_arbitrary_raster = r'UI_polygon_filepath'
        #read_raster = gpd.read_file(in_arbitrary_raster)
        #vector_in_raster = read_raster.head()
        #nums_list_bounds.append(vector_in_raster)

        print(total)

        raster_mean_function = sum(nums_list_bounds) / len(nums_list_bounds)
        return raster_mean_function
        print(raster_mean_function)

        ###Exploring raster file data and metadata
        ###Note what transformaitons are required during the task

        #Find cell width and height
        ds_3.meta
        #file name
        ds_3.name
        #bands in file
        ds_3.count
        ds_3.shape
        ds_3.width
        ds_3.height
        # should return 'GTiff'
        ds_3.driver
        ds_3.crs
        ds_3.descriptions
        data.size
        dtype('uint8')
        data.min()
        data.min()

    #long approach to get average
        total = 0
        for i in nums_list:
            total += i #shorthand: total = total + i



def filepath(read_geojson)
def filepath(read_shp)
def filepath(read_TIFF)

# Option_2 = read_shp


#len(read_geojson)
#read_geojson.crs
#read_geojson.geom_type
#read_geojson.plot()

#read_geojson = gpd.read_file(in_geojson)
#read_geojson.head()
# Option_1 = read_geojson


def arbitrary_raster():
    arbitrary_filepath = (input("insert filepath: "))

    # if 

    vector_polygon_filepath = (input("Launching...would you like to open read_geojson Y/N: "))

    if vector_polygon_filepath == Y:
       

        ###my_list = read_geojson.head()
        ###average = (sum(str(my_list))) / (int(len(my_list)))
        print(average)

        len(read_geojson)
        read_geojson.crs
        read_geojson.geom_type
        read_geojson.plot()
    else:
        print(filepath)
        break

def vector_polygon():
  # This vector polygon = [] should exist outside the function so it can retain values between calls.
    if point == 0:
        print("No data provided!")
    else:
        filepath.average(point)
        print("Average value of cells is ${point} added.")

    point = int(input(Point(float(position_long_degrees), float(position_lat_degrees))))
    print(f"average value of ${cells} within the polygon.")
    #f-string to display the actual amount entered (${cells})
    break

        
arbitrary_raster()
