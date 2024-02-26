import streamlit as st
import requests

# API parameters
api_key = "gamrBaDSgHEIgNLg5BjcQ42bFqKzpceDPsB8F0fQ"
url = "https://api.nasa.gov/planetary/apod" \
       f"apiKey={api_key}"

# Make a request
request = requests.get(url)


st.title("App to show the astronomy image of the day")
# st.image()
st.write("Description")
