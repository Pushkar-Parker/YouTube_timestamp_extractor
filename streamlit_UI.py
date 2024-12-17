import streamlit as st
from timestamps import processed_timestamps
from pyperclip import copy
# Center the title
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 2em;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        width: 100%;
        margin: 0 auto;
        display: block;
    }
    .stButton > button {
        margin: 0 auto;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# Set the title of the app
st.markdown('<div class="title">YouTube Timestamps Extractor</div>', unsafe_allow_html=True)

# Add a wide text input bar for the YouTube link
link = st.text_input("", placeholder="Paste YouTube link here", label_visibility="hidden")

# Add a button below the text input
if st.button("Get Timestamps!"):
    if link.strip():
        st.write(f"Processing timestamps for: {link}")
        timestamps = processed_timestamps(link)

        for data in timestamps:
            st.write(f"{data} : {timestamps[data]}")
            
    else:
        st.error("Please paste a valid YouTube link.")
