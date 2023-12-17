import streamlit as st
import geopandas as gpd
import pandas as pd

import numpy as np
import folium


from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


from ipyleaflet import Map, SplitMapControl, TileLayer

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


# Title and Description
st.title("Classification maps")
st.info('Explore the maps that are derived from different approaches .. In the sidebar , choose the image to classify and the Method')
dst_crs = 'EPSG:4326'
selected_day = st.sidebar.selectbox('Select Day:', ['16-17', '22-23'] )
selected_attribute = st.sidebar.selectbox('Select method', ['Decision_Tree', 'A_Neurol_Net', 'Index_combinaison','SVM','Smile_Cart','RandomForest'])
image_path = f"https://rihi22.github.io/image/{selected_attribute}{selected_day}.tif"
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

legend_dict = {
    "eau": "#16dcea",
    "sol": "#a8483d",
    "Végétation": "#179d1e",
    
}

style = {
    'position': 'fixed',
    'z-index': '9999',
    'border': '2px solid grey',
    'background-color': 'rgba(255, 255, 255, 0.8)',
    'border-radius': '10px',
    'padding': '5px',
    'font-size': '14px',
    'bottom': '20px',
    'right': '5px',}


    

m = leafmap.Map(location=[33.884371, -6.730471], zoom_start=12)
m.add_legend(title='Legende', legend_dict=legend_dict, draggable=False, style=style)
m.add_child(folium.raster_layers.ImageOverlay(img.transpose(1, 2, 0), opacity=.7,
                                              bounds=bounds_fin))
    
folium_static(m)