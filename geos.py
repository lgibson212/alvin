import pandas as pd
import geocoder
import googlemap
import geopandas
import geojson
from shapely.geometry import Point
from geopandas import GeoDataFrame
from geojson import Feature, FeatureCollection
from geojsonio import display
#https://github.com/lesley2958/data-blog/tree/master/NYC%20alvin




# authentication initialized, different syntax for each API, read API doc
gmaps = googlemaps.Client(key='my_key')


#open csv with list of bubble tea places in NYC
#data needs to be saved in csv. address column super important! used to get lat/long
alvin=pd.read_csv('./alvin.csv')

alvin['Lat'] = alvin['Address'].apply(geocoder.google).apply(lambda x: x.lat)
alvin['Long'] = alvin['Address'].apply(geocoder.google).apply(lambda x: x.lng)

# writes to a csv and opens
alvin.to_csv('alvin_final.csv')
alvin = pd.read_csv('./alvin_final.csv')

# converts lat and long points to coordinate point data type
geo = [Point(xy) for xy in zip(alvin.Longitude, alvin.Lat)]

# sets to geodataframe
#crs = coordinates reference system- google uses epsg:4326
crs = {'init': 'epsg:4326'}

#gets alvin place name from csv/df
site=alvin['Name']

#geodataframe parameters in documentation
geo_df = GeoDataFrame(site, crs=crs, geometry=geo) 

# fixes json formatting and puts it back into geodataframe
#listcomprehension to serialize json - a list of the dict
# would not need these two lines if json was correct format
l1 = [geojson.dumps(i, sort_keys=True) for i in geo] 
geo_df = GeoDataFrame(l1, crs=crs, geometry=geo) 

# displays to geojsonio
display(geo_df.to_json())

