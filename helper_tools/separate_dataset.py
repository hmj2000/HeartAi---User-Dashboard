# Import necessary libraries
import os
import shutil
from sklearn.model_selection import train_test_split

# Define your dataset directory
dataset_dir = '/home/hamza/Documents/HeartAi/dataset'  # Path to your .wav files
output_train_dir = '/home/hamza/Documents/HeartAi/train'  # Path for training set
output_test_dir = '/home/hamza/Documents/HeartAi/test'  # Path for testing set

# Ensure the output directories exist
os.makedirs(output_train_dir, exist_ok=True)
os.makedirs(output_test_dir, exist_ok=True)

# List all audio files
all_files = [f for f in os.listdir(dataset_dir) if f.endswith('.wav')]

# Split dataset into training and testing sets
train_files, test_files = train_test_split(all_files, test_size=0.2, random_state=42)

# Copy files to the respective directories
for f in train_files:
    shutil.copy(os.path.join(dataset_dir, f), os.path.join(output_train_dir, f))

for f in test_files:
    shutil.copy(os.path.join(dataset_dir, f), os.path.join(output_test_dir, f))

print(f"Training set size: {len(train_files)}, Test set size: {len(test_files)}")
