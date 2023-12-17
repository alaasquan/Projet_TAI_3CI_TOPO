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
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie

team='https://rihi22.github.io/drought/Team.json'


def load_lottiefile(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses
    return response.json()


def load_lottirurl(url: str):
	r= requests.get(url)
	if r.status_code != 200:
		return None
	return r.json

lottie_team=load_lottiefile(team)

st.title('Reach the team !')
st.write(
        "This project was developed as part of the Image Processing course in the 3rd year of Topographic Engineering and Geomatics Science. The course is taught by Professor Mme Imane Sebari, and this platform was created by the following students"
    )
col1,col2=st.columns(2)
with col1:
    st.write("**HAMZAOUI HAJAR**")
    st.write("📧 Email: hajarhamzaoui235@gmail.com")

    st.write("**MADICH BADER**")
    st.write("📧 Email: badermadich2001@gmail.com")

with col2:
    st.write("**RIHI MERYAME**")
    st.write("📧 Email: rihimerymaegeo@gmail.com")

    st.write("**SAQOUANE ALAA**")
    st.write("📧 Email: alaasaqouane@gmail.com")


col1,col2, col3=st.columns(3)
with col1:
      st.write('')
with col2:
      
      st_lottie(lottie_team,
        speed= 1,
        reverse=False,
        loop=True,
        quality='low',
        height='150px',
        width='150px',)
      
with col3:
      st.write('')