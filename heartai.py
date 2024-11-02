import numpy as np
import librosa
import librosa.display
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import os

# Load pre-trained model
model_path = 'heart_model.h5'
model = load_model(model_path)

def extract_features(file_path):
    """
    Extracts Mel-spectrogram features from a given audio file.
    """
    y, sr = librosa.load(file_path, sr=22050)
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    return spectrogram_db

def predict_heart_condition(file_path):
    """
    Predicts the heart condition based on the spectrogram features.
    """
    features = extract_features(file_path)
    features = np.expand_dims(features, axis=(0, -1))  # Shape for model input: (1, height, width, 1)
    prediction = model.predict(features)
    return "Abnormal" if prediction > 0.5 else "Normal"
