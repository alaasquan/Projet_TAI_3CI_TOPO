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

def main():
          st.title("Split-panel Map")
          
          st.info('Through Split Map Page , assess the difference of water body as well as other classes between the period of 2016/2017 and 2022/2023')
    
    # Sélecteurs pour les jours gauche et droit
          
          selected_attribute = st.sidebar.selectbox('Select method', ['Decision_Tree', 'A_Neurol_Net', 'Index_combinaison','SVM','Smile_Cart','RandomForest'])
          left_jour_key = '16-17'
          right_jour_key = '22-23'
          left_image_url = f"https://rihi22.github.io/image/{selected_attribute}{left_jour_key}.tif"
          right_image_url = f"https://rihi22.github.io/image/{selected_attribute}{right_jour_key}.tif"
          st.sidebar.markdown(f"**Left Image Date:** 2016-2017")
          st.sidebar.markdown(f"**Right Image Date:** 2022-2023")
          m = leafmap.Map()
          m.split_map(left_image_url, right_image_url)
          m.to_streamlit(height=700)

if __name__ == "__main__":
          main()