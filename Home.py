import streamlit as st
import requests

# API parameters
api_key = "gamrBaDSgHEIgNLg5BjcQ42bFqKzpceDPsB8F0fQ"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}&" \
      "date=2024-02-25"

# Make a response, get the data
response1 = requests.get(url)
data = response1.json()

# Get the title, image url, and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "image.png"
response2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
