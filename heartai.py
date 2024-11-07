import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'heart_model.h5')
SPECTROGRAM_DIR = os.path.join(BASE_DIR, 'spectrograms')
os.makedirs(SPECTROGRAM_DIR, exist_ok=True)

model = load_model(MODEL_PATH)

def extract_features(file_path):
    audio, sr = librosa.load(file_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr, n_mels=128, fmax=8000)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    
    image_path = os.path.join(SPECTROGRAM_DIR, os.path.basename(file_path).replace('.wav', '.png'))
    plt.figure(figsize=(5, 5))
    librosa.display.specshow(spectrogram_db, sr=sr, hop_length=512)
    plt.axis('off')
    plt.savefig(image_path, bbox_inches='tight', pad_inches=0)
    plt.close()
    
    return spectrogram_db, image_path

def predict_heart_condition(file_path):
    features, image_path = extract_features(file_path)
    features = np.expand_dims(features, axis=(0, -1))
    prediction = model.predict(features)[0][0]
    label = 'Abnormal' if prediction > 0.5 else 'Normal'
    return {'prediction': label, 'spectrogram_image': image_path}
