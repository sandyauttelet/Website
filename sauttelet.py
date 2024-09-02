# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:04:37 2024

@author: sandy
"""

from PIL import Image
import requests
import streamlit as st

st.set_page_config(page_title="sauttelet", page_icon=":globe_with_meridians:", layout="wide")

#---Assets---
img_headshot = Image.open("images/Headshot_sandy.png")
cv1 = Image.open("images/cv1.png")
cv2 = Image.open("images/cv2.png")
cv3 = Image.open("images/cv3.png")
cv4 = Image.open("images/cv4.png")
min_cut = Image.open("images/2D_min_cut.png")

#---Use local CSS---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#---Home Page---
def main_page():
    st.markdown("# Home")
    st.sidebar.markdown("# Home")
    st.subheader("Hi, I am Sandy Auttelet")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_headshot)
    with text_column:
        st.title("Bachelor of Science in Physics and Theoretical Mathematics")
        st.write("I am interested in pursuing a PhD in Geometric Theoretical Physics")
    

#---CV Page---
def page2():
    st.markdown("# CV")
    st.sidebar.markdown("# CV")
    st.image(cv1)
    st.image(cv2)
    st.image(cv3)
    st.image(cv4)

#---Research Page---
def page3():
    st.markdown("# My Current Research Interests")
    st.sidebar.markdown("# Research")
    with st.container():
        st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.image(min_cut)
    with right_column:
        st.write("Flat norm text")

#---Projects Page---
def page4():
    st.markdown("# Projects")
    st.sidebar.markdown("# Projects")
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.empty()
    with text_column:
        st.write("Write some information about each project")
        st.markdown("[Project report and code](https://github.com/sandyauttelet)")

#---Contact Page---
def page5():
    st.markdown("# Contact Me")
    st.sidebar.markdown("# Contact Me")
    with st.container():
        st.write("---")
        st.header("Get in touch with me!")
        st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/sandyauttelet1@gmail.com" method="POST">
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

page_names_to_funcs = {
    "Home": main_page,
    "CV": page2,
    "Research": page3,
    "Projects": page4,
    "Contact": page5,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
