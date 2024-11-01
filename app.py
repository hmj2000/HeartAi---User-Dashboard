from flask import Flask, request, jsonify, send_from_directory
import os
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Database setup
conn = sqlite3.connect('heart_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS recordings (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                file_path TEXT,
                analysis_result TEXT
            )''')
conn.commit()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Placeholder for ML model analysis integration
    analysis_result = "Analysis pending"

    # Save to DB
    user_id = request.form.get('user_id')  # Adjust based on your frontend setup
    c.execute("INSERT INTO recordings (user_id, file_path, analysis_result) VALUES (?, ?, ?)",
              (user_id, file_path, analysis_result))
    conn.commit()

    return jsonify({"message": "File uploaded successfully", "file_path": file_path, "analysis_result": analysis_result})

@app.route('/get_recordings/<user_id>', methods=['GET'])
def get_recordings(user_id):
    c.execute("SELECT * FROM recordings WHERE user_id=?", (user_id,))
    recordings = c.fetchall()
    return jsonify(recordings)

if __name__ == '__main__':
    app.run(debug=True)
