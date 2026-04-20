import streamlit as st
import pandas as pd

Name = st.text_input("Enter your Name:")
FName = st.text_input("Enter your father's Name:")
adr = st.text_area("Enter your Text:")
classdata = st.selectbox("Enter your class:",(10,11,12,'Graduate'))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name :{Name}
    Father's Name:{FName}
    Address:{adr}
    Class data:{classdata}""")