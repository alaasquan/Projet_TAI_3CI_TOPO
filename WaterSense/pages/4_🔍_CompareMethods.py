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
def main():
        st.title("Split-panel for Methods comparison")
        st.info('Through Split Map Page , assess difference of the classification methods')
    # Selector for the day
        selected_day = st.sidebar.selectbox("Select the day", ['16-17', '22-23'])
    
    # Selector for the left image method
        left_method = st.sidebar.selectbox('Select method for left image', ['Decision_Tree', 'A_Neurol_Net', 'Index_combinaison', 'SVM', 'Smile_Cart', 'RandomForest'])
    
    # Generate a list of available methods for the right image
        available_methods = [method for method in ['Decision_Tree', 'A_Neurol_Net', 'Index_combinaison', 'SVM', 'Smile_Cart', 'RandomForest'] if method != left_method]
    
    # Selector for the right image method
        right_method = st.sidebar.selectbox('Select method for right image', available_methods)
    
    # Generate image URLs based on the selected day and methods
        left_image_url = f"https://rihi22.github.io/image/{left_method}{selected_day}.tif"
        right_image_url = f"https://rihi22.github.io/image/{right_method}{selected_day}.tif"
    
    # Create and display the split-panel map
        m = leafmap.Map()
        m.split_map(left_image_url, right_image_url)
        m.to_streamlit(height=700)

if __name__ == "__main__":
        main()
