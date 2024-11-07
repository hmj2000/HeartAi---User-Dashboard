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
    with open(os.path.join(UPLOAD_FOLDER, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.write(f"File '{uploaded_file.name}' uploaded successfully.")

    response = requests.post("http://localhost:5000/upload", files={'file': uploaded_file})

    if response.status_code == 200:
        result = response.json()
        st.write(f"Prediction: {result.get('prediction', 'Result unavailable')}")
        if 'spectrogram_image' in result:
            st.image(result['spectrogram_image'])
    else:
        st.write(f"Error: {response.json().get('error')}")
