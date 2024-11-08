import streamlit as st
import requests
import os

# Relative path for uploads folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.title("Heart Sound Analysis App")
st.header("Upload Your Heart Sound Recording for Analysis")

uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"File '{uploaded_file.name}' uploaded successfully.")

    backend_url = os.getenv("BACKEND_URL")
    if backend_url:
        # Open the file in binary mode to send in the request
        with open(file_path, "rb") as file:
            response = requests.post(f"{backend_url}/upload", files={'file': file})

        if response.status_code == 200:
            try:
                data = response.json()
                st.write(f"Success: {data}")
            except ValueError:
                st.write("Error: The server did not return JSON data.")
        else:
            st.write(f"Error: {response.status_code} - {response.text}")
    else:
        st.write("Error: BACKEND_URL environment variable not set.")
