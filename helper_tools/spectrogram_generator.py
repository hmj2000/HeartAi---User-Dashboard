# Import necessary libraries
import os
import librosa
import librosa.display
import numpy as np  # Make sure this is imported
import matplotlib.pyplot as plt

# Define input and output directories
input_dir = '/home/hamza/Documents/HeartAi/train'  # Path to the training set folder
output_dir = '/home/hamza/Documents/HeartAi/spectrograms'  # Path to save spectrograms
os.makedirs(output_dir, exist_ok=True)

# Generate spectrograms for all audio files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.wav'):
        file_path = os.path.join(input_dir, file_name)
        y, sr = librosa.load(file_path, sr=None)
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)

        # Plot and save the spectrogram as an image
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='mel')
        plt.colorbar(format='%+2.0f dB')
        plt.title(f'Spectrogram of {file_name}')
        plt.tight_layout()
        output_file_path = os.path.join(output_dir, f'{file_name}.png')
        plt.savefig(output_file_path)
        plt.close()

print("Spectrogram generation complete.")
