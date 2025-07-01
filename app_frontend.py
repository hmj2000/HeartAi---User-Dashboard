import streamlit as st
import requests
from PIL import Image
import io
import os

# Set the URL for the Flask backend
backend_url = "https://heartai-backend-production.up.railway.app"

# Set up the uploads folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')

# Ensure Uploads Folder Exists Safely
if os.path.exists(UPLOAD_FOLDER):
    if not os.path.isdir(UPLOAD_FOLDER):
        raise Exception(f"A file named 'uploads' exists. Please delete or rename it.")
else:
    os.makedirs(UPLOAD_FOLDER)

# UI Layout
st.title("Heart Sound Analysis App")
st.header("Upload Your Heart Sound Recording for Analysis")

uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None:
    # Save the uploaded file locally
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"File '{uploaded_file.name}' uploaded successfully.")
    st.audio(uploaded_file, format="audio/wav")

    # Send the file to the Flask backend
    if backend_url:
        with st.spinner("Analyzing heart sound..."):
            try:
                with open(file_path, "rb") as file:
                    response = requests.post(f"{backend_url}/upload", files={'file': file})

                if response.status_code == 200:
                    try:
                        data = response.json()
                        st.write("Analysis Result:", data.get("prediction", "Unknown"))

                        # Display the analyzed spectrogram image
                        image_url = f"{backend_url}/download/{uploaded_file.name.replace('.wav', '_analyzed.png')}"
                        image_response = requests.get(image_url)

                        if image_response.status_code == 200:
                            image = Image.open(io.BytesIO(image_response.content))
                            st.image(image, caption="Analyzed Spectrogram")
                        else:
                            st.write("Error: Could not retrieve the analyzed spectrogram image.")
                    except ValueError:
                        st.write("Error: The server did not return valid JSON.")
                else:
                    st.write(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.write(f"Error connecting to backend: {e}")
    else:
        st.write("Error: BACKEND_URL is not set.")
