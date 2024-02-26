import streamlit as st
import requests

# API parameters
api_key = "gamrBaDSgHEIgNLg5BjcQ42bFqKzpceDPsB8F0fQ"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}&" \
      "date=2024-02-25"

# Make a request
request = requests.get(url)

# Get a dictionary with the data
content = request.json()

# Get an image url and download it
image_url = content["url"]
response = requests.get(image_url)
with open("image.jpg", "wb") as file:
    file.write(response.content)

# Get the description
description = content["explanation"]

st.title("App to show the astronomy image of the day")
st.image("image.jpg")
st.write(description)
