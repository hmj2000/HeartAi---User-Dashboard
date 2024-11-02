# app_frontend.py - Streamlit frontend code
import streamlit as st
import requests

# Set up the title and header
st.title("Heart Sound Analysis App")
st.header("Upload Your Heart Sound Recording for Analysis")

# File uploader component
uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

# Button for file upload and analysis
if uploaded_file is not None:
    # Display file upload confirmation
    st.write(f"File '{uploaded_file.name}' uploaded successfully.")
    
    # Send the uploaded file to the backend
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    try:
        response = requests.post("http://localhost:5000/upload", files=files)

        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"Analysis Result: {result}")
        else:
            error_message = response.json().get("error", "An unknown error occurred.")
            st.error(f"Error: {error_message}")
    except Exception as e:
        st.error(f"Error connecting to the backend: {str(e)}")

# Optional: add further explanation or insights for users
st.write("Note: This tool analyzes heart sound recordings and classifies them as 'Normal' or 'Abnormal'.")
