from flask import Flask, request, jsonify
from flask_cors import CORS
from heartai import predict_heart_condition
import os

app = Flask(__name__)
CORS(app)

# Relative path for uploads folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        prediction = predict_heart_condition(file_path)
        return jsonify(prediction), 200

if __name__ == '__main__':
    app.run(debug=True)
