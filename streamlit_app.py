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

st.markdown("<h1 style='text-align: center; color: white;'>Days Until V2 </h1>", unsafe_allow_html=True)


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

var countDownDate = new Date("Apr 14, 2023 00:00:00").getTime();


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
                webbrowser.open("https://www.linkedin.com/in/adrian-m/")
        with col2:
            if st.button("Github:computer:"):
                webbrowser.open("https://github.com/amyers498")   
        with col3:
            if st.button("My Resume/CV:scroll:"):
                webbrowser.open("https://www.linkedin.com/in/adrian-m/overlay/1635516621678/single-media-viewer/?profileId=ACoAACzeli0BrK_8ieR3vyBJRiUX_AA2awrGE0E") 


    with right_column:
        st.image("BE231B4C-F280-414F-9073-62E5DFDD1F3A.jpg", width = 400 )
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About")
        st.write("##")
        st.write( """
        I thank you for visiting my website. This website is created using Python and a framework called Streamlit.
        The current design and state of this website is the product of me using this framework for the first time. 
        Over the next 6 months I plan on consistently updating this website to display my skills and orijects to ultimately serve as
        a portfolio site. I am passionate of the intersection where business meets data and technology and that is what I want to be displayed on my porrtfolio site.
        
        
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




