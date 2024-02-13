import requests
import streamlit as st
from streamlit_lottie import st_lottie 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from streamlit.components.v1 import html
import webbrowser
#this library is used for allowing buttons redirect to another website
from bokeh.models.widgets import Div




#basic config of website
st.set_page_config(page_title="Adrian's Portfolio", page_icon=":wave:",layout="wide")

#loading lottie animation)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
##animation
Data = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_ps1145pz.json")
Waving = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_F2Mv1p.json")

st.markdown("<h1 style='text-align: center; color: white;'>Portfolio Project V1</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Days Until V3 </h1>", unsafe_allow_html=True)


Countdown_html = """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
p {
  font-family: Sans-Serif;
  text-align: center;
  font-size: 60px;
  margin-top: 0px;
  color: white;
}

</style>
</head>
<body>


<p id="demo"></p>

<script>

var countDownDate = new Date("June 30, 2024 00:00:00").getTime();


var x = setInterval(function() {

  var now = new Date().getTime();

  var distance = countDownDate - now;
  
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
  
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);
</script>

</body>
</html>

"""

html(Countdown_html)


## Physically showing Animation
st_lottie(Waving, height =100, key="waving")






with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        
        st.title("Hi I am Adrian:wave:")
    
        st.subheader("A Business Analytics Student from Florida Polytechnic University")
        st.write("I strive to use my knowlege of data and business to solve problems and make deals!")
        col1, col2, col3 = st.columns([.5,.5,.5])
        with col1:
            if st.button("My Linkedin:open_file_folder:"):
               
                js = "window.open('https://www.linkedin.com/in/adrian-m/')"  # New tab or window
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)
                
        with col2:
            if st.button("Github:computer:"):
                js = "window.open('https://github.com/amyers498')"  # New tab or window
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)  
        with col3:
            if st.button("My Resume/CV:scroll:"):
                js = "window.open('https://www.linkedin.com/in/adrian-m/overlay/1707779643190/single-media-viewer/?profileId=ACoAACzeli0BrK_8ieR3vyBJRiUX_AA2awrGE0E')"  # New tab or window
                html = '<img src onerror="{}">'.format(js)
                div = Div(text=html)
                st.bokeh_chart(div)   
                
           
    with right_column:
        st.image("BE231B4C-F280-414F-9073-62E5DFDD1F3A.jpg", width = 400 )
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About")
        st.write("##")
        st.write( """
       
Thank you for taking the time to explore my website. I've built this platform using the Streamlit framework, leveraging Python to create a seamless user experience. This iteration, V2, introduces an intuitive admin control panel, enabling effortless adjustments to settings and text information without the need for manual code modifications.

Driven by my passion for coding, I specialize in harnessing the power of data libraries to tackle real-world problems. My goal is to utilize data-driven approaches to solve complex challenges and make informed decisions. Feel free to navigate through my portfolio page to discover more about my projects and expertise.
        
        
        """)
    with right_column:
        st_lottie(Data, height =300, key="coding")
with st.container():
    st.write("---")
    st.title("UFO Project (An Analysis of UFO Sightings)")
    st.write(""" 
        This project was about taking given data "cleaning it up" 
        and organizing it to find "fun" facts about UFO Sightings.


        """)
    left_column, right_column = st.columns(2)
    with left_column:
        # Python Code for UFO Project 
        ufo_df = pd.read_csv('ufo.csv')
        ufo_df.at[35692, 'duration (seconds)'] = 8
        ufo_df.at[58591, 'duration (seconds)'] = 0.5
        ufo_df.at[27822, 'duration (seconds)'] = 2
        st.subheader('All Data Points')
        ufo_df
        ufo_df['shape'].value_counts()
        light_shape_df = ufo_df.loc[ufo_df['shape']=='light']
        light_shape_df['state'].value_counts()
    with right_column:   
        st.subheader('Sightings where "shape" = "light"')
        light_shape_df
    with left_column:
       shape_count = ufo_df['shape'].value_counts()
       st.subheader("Number of Times Each Shape was Sighted")
       shape_count
       
        
    with right_column:   
        citycounts_df = ufo_df['city'].value_counts()
        st.subheader("Amount of UFO's Sighted in Each City")
        
        citycounts_df
    with left_column:
        #allowing pdf to be downloaded
        with open("UFOProject.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
# download button
        st.download_button(label="Download FULL WRITTEN UFO ANALYSIS", 
                data=PDFbyte,
                file_name="UFOProject.pdf",
                mime='application/octet-stream')
    ## fun buttons
    with right_column:
        if st.button("CLICK ME"):
            st.snow()
        if st.button("CLICK ME TOO"):
            st.balloons()




