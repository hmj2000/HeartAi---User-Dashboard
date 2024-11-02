import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import load_img, img_to_array

# Set directories
spectrogram_dir = '/home/hamza/Documents/HeartAi/spectrograms'
image_size = (128, 128)  # Adjust based on your spectrogram size

# Load and preprocess data
X = []
y = []
for file_name in os.listdir(spectrogram_dir):
    if file_name.endswith('.png'):
        label = 0 if 'normal' in file_name else 1  # Adjust labeling logic as needed
        img_path = os.path.join(spectrogram_dir, file_name)
        img = load_img(img_path, color_mode='grayscale', target_size=image_size)
        img_array = img_to_array(img) / 255.0  # Normalize to [0, 1]
        X.append(img_array)
        y.append(label)

X = np.array(X)
y = np.array(y)

# Split data into training and testing sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary classification (adjust for multi-class if needed)
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save the trained model
model.save('/home/hamza/Documents/HeartAi/heart_model.h5')

print("Model training complete and saved as 'heart_model.h5'")
