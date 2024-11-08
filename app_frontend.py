import streamlit as st
import requests
import os

# Define the URL of the Flask backend hosted on Replit
backend_url = "https://516299ad-8520-43fc-8c68-ea6726ba6def-00-22s50ndij9nvh.spock.replit.dev"

# Create a folder to store uploaded files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Streamlit UI
st.title("Heart Sound Analysis App")
st.header("Upload Your Heart Sound Recording for Analysis")

# File uploader widget
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None:
    # Save the uploaded file locally in the uploads folder
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write(f"File '{uploaded_file.name}' uploaded successfully.")

    # Send the file to the Flask backend
    if backend_url:
        with open(file_path, "rb") as file:
            response = requests.post(f"{backend_url}/upload", files={'file': file})

        # Process the backend response
        if response.status_code == 200:
            try:
                data = response.json()
                st.write("Analysis Result:", data)
            except ValueError:
                st.write("Error: The server did not return JSON data.")
        else:
            st.write(f"Error: {response.status_code} - {response.text}")
    else:
        st.write("Error: BACKEND_URL is not set.")
