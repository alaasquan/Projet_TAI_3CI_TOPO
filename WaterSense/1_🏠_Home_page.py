import streamlit as st
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Home page",
    page_icon="🏠",
)

world_anim= 'https://alaasquan.github.io/Streamlit_app/Dashboard_Streamlit/Animation_Lottiefiles/Worldmap.json'
WaterHome='https://rihi22.github.io/drought/watercontact.json'
grou= 'https://rihi22.github.io/drought/grou.jpeg'

def load_lottiefile(url: str):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad responses
    return response.json()


def load_lottirurl(url: str):
	r= requests.get(url)
	if r.status_code != 200:
		return None
	return r.json

lottie_World_map=load_lottiefile(world_anim)
lottie_WaterHome=load_lottiefile(WaterHome)

# Add animation CSS
st.markdown(
    """
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.title("WaterSense")


# Add animation CSS
# CSS styles for animations
css_styles = """
<style>
.bounce {
    animation: bounce 2s infinite;
    font-weight: bold; /* Bold text */
    font-size: 20px;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-20px);
    }
    60% {
        transform: translateY(-10px);
    }
}

.bg-title {
    background-color: #2d4059; /* Background color for titles */
    color: white; /* Text color for titles */
    padding: 5px 10px;
    display: inline-block;
    margin-bottom: 10px;
}

.typing-text {
    overflow: hidden;
    white-space: nowrap;
    animation: typing 3s steps(20, end) infinite;
}

@keyframes typing {
    from {
        width: 0;
    }
    to {
        width: 100%;
    }
}
</style>
"""
st.markdown(
    """
    <style>
        .bg-title {
            font-size: 20px ;
            color: black; /* Text color for titles */
            padding: 5px 10px;
            display: inline-block;
            margin-bottom: 5px;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Display CSS styles
st.markdown(css_styles, unsafe_allow_html=True)

# Project Description
st.write(""" ### Welcome 👋🏻""")
# Create two text columns
col1, col2 = st.columns(2)

# Text for column 1
with col1:
    st.write("""Welcome to our Water Body Drought Detection Project : WaterSense 🛰️!
              In a world facing unprecedented climate change, the crucial theme of water has taken center stage. Now, more than ever, water resources are experiencing alarming situations of drought. Our project delves into the heart of this matter, exploring the impact of excessive climate change on water bodies.   
    """)
# Text for column 2
with col2:

    st_lottie(lottie_WaterHome,
	   speed= 1.5,
	   reverse=False,
	   loop=True,
	   quality='low',
	   height='250px',
	   width='250px',)



### 
st.write("""
         
### Objectives:        
  - **Analytical Insight:** Apply diverse satellite imagery classification approaches, employing various photogrammetry solutions. This includes utilizing neural network techniques in ENVI, machine learning algorithms in Google Earth Engine, and leveraging Ecognition for comprehensive analysis.
 - **Georeferenced Mapping:** Develop georeferenced maps to visually depict and quantify the severity of drought affecting water bodies.

- **Accessibility:** Transform our research findings into an interactive web app, making the information easily accessible to a diverse audience.

- **Awareness and Understanding:** Contribute to the public understanding of water scarcity issues by presenting clear and comprehensive information through the web app.

- **Emergency Call for Action:** Issue an urgent call for action by providing tangible evidence of drought impact through raster maps and quantitative assessments of water body drought.
""")

("""
    ### 📚Case study Overview- Oued Grou""")
col1, col2 = st.columns(2)

# Text for column 1
with col1:

    st.write("""This study focuses specifically on applying advanced techniques to detect drought-prone areas along the Oued Grou, anticipating their significant impact on the water availability of the Ben Abdellah Dam in Rabat.""")
    st.write("""Find the localisation of our study area here , see link 👉🏻[here](https://www.google.com/maps/place/Barrage+Mohamed+Ben+Abdellah/@33.9109656,-6.7135,12z/data=!4m6!3m5!1s0xda73f5d2d497eeb:0x47c9c6ba762c533f!8m2!3d33.9653969!4d-6.7012424!16s%2Fg%2F1tgqkshx?entry=ttu) """)

with col2: 

    st.image(grou, caption='Oued Grou', use_column_width=True)
("""
### 💦Project Context
Born from a group brainstorming session, this project aims to apply varied image processing and classification methods. Focusing on change detection, we've honed in on the Oued Grou watershed in the expansive Bouregreg basin, critical due to its connection to the Mohammed ben Abdellah Dam. This dam is currently linked with Sebou Dam, responding to water scarcity concerns. The study illuminates the drought from 2016 to 2023, a critical period for our nation's water resources.

""")


