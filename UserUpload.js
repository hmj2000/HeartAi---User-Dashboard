import React, { useState } from 'react';
import axios from 'axios';

function UserUpload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);
    formData.append("user_id", "exampleUserID"); // Replace with dynamic user ID

    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      alert(response.data.message);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default UserUpload;
