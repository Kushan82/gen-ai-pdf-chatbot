import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]

for file in list_of_files:
    file_path = Path(file)
    filedir, filename = os.path.split(file_path)

    # These blocks must be inside the loop
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass # 'pass' creates an empty file
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}") # Changed to include full path for clarity