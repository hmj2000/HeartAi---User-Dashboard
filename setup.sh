
### `setup.sh`
```bash
#!/bin/bash

# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Update pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Install additional dependencies (if not listed in requirements.txt)
pip install librosa matplotlib tensorflow scikit-learn streamlit flask flask-cors

# Inform the user
echo "Setup completed successfully. Run 'source venv/bin/activate' to activate your environment."

