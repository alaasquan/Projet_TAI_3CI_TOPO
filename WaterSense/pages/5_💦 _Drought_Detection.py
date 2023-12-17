import streamlit as st
import geopandas as gpd
import pandas as pd

import numpy as np
import folium


from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import geemap
from ipyleaflet import Map, SplitMapControl, TileLayer
from geemap import foliumap
from rasterio.transform import from_origin
from rasterio.enums import Resampling
import rasterio
import imageio
from folium import plugins
from folium.plugins import MarkerCluster
import leafmap.foliumap as leafmap
import rasterio as rio
from pyproj import Transformer
import folium
from streamlit_folium import folium_static
from branca.colormap import LinearColormap
from rasterio.windows import Window

st.title('Drought Detection')
st.info("""Through this Page , visualise the affected water areas dy drought.
          A pixel count was conducted to assess the area of water affected by drought. The number of pixels amounts to 9,784 pixels. Given a spatial resolution of 10 meters, this corresponds to an area of approximately 978,466.67 square meters, or approximately 97.85 hectares.""")
dst_crs = 'EPSG:4326'

image_path = "https://rihi22.github.io/drought/drought.tif"
with rio.open(image_path) as src:
          img = src.read()
          src_crs = src.crs.to_string().upper()
          min_lon, min_lat, max_lon, max_lat = src.bounds

bounds_orig = [[min_lat, min_lon], [max_lat, max_lon]]

bounds_fin = []
for item in bounds_orig:
          lat = item[0]
          lon = item[1]

          proj = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

          lon_n, lat_n = proj.transform(lon, lat)

          bounds_fin.append([lat_n, lon_n])

centre_lon = bounds_fin[0][1] + (bounds_fin[1][1] - bounds_fin[0][1]) / 2
centre_lat = bounds_fin[0][0] + (bounds_fin[1][0] - bounds_fin[0][0]) / 2
m = folium.Map(location=[33.884371, -6.730471], zoom_start=12)
folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', name='Esri.WorldImagery' ,attr="Esri.WorldImagery").add_to(m)
m.add_child(folium.raster_layers.ImageOverlay(img.transpose(1, 2, 0), opacity=.7,
                                              bounds=bounds_fin))

folium_static(m)