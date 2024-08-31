# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:04:37 2024

@author: sandy
"""

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="sauttelet", page_icon=":globe_with_meridians:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---Use local CSS---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

#---Assets---
lottie_geometry = load_lottieurl("https://lottie.host/f06e07de-6fa1-46fe-8fdf-cb2ccd113962/7pjmEm0T2j.json")
img_headshot = Image.open("images/Headshot_sandy.png")

st.subheader("Hi, I am Sandy Auttelet")
st.title("Bachelor of Science in Physics and Theoretical Mathematics")
st.write("I am interested in pursuing a PhD in Geometric Theoretical Physics")
st.write("[Projects Found Here](https://github.com/sandyauttelet)")

#---What I do---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
    with right_column:
        st_lottie(lottie_geometry, height=300, key="geometry")
        
#---Projects---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_headshot)
    with text_column:
        st.write("Write some information about each project")
        st.markdown("[Project report and code](https://github.com/sandyauttelet)")
        
#---Contact form---
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/sandra.zichterman@wsu.edu" method="POST">
    <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
