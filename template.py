import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Ai_Recruit_Assist"

list_of_files = [
    ".github/workflows/.gitkeep",  # For CI/CD pipeline
    f"src/{project_name}/__init__.py",  # Package initialization
    f"src/{project_name}/components/__init__.py",  # Components for modular code
    f"src/{project_name}/components/candidate_screening.py",  # Screening logic
    f"src/{project_name}/components/email_handler.py",  # Email writing and sending
    f"src/{project_name}/utils/__init__.py",  # Utility functions
    f"src/{project_name}/utils/pdf_processor.py",  # PDF extraction
    f"src/{project_name}/utils/groq_client.py",  # Groq API client
    f"src/{project_name}/config/__init__.py",  # Configuration management
    f"src/{project_name}/config/configuration.py",  # Config class
    f"src/{project_name}/constants/__init__.py",  # Constants
    f"src/{project_name}/constants/constants.py",  # Constant values
    "app.py",  # Streamlit app entry point
    "config/config.yaml",  # Configuration file
    "requirements.txt",  # Dependencies
    "setup.py",  # Setup script for package
    "Dockerfile",  # Docker configuration for deployment
    ".env",  # Environment variables
    "README.md",  # Project documentation
    "tests/__init__.py",  # Test package
    "tests/test_screening.py",  # Unit tests for screening
    "templates/email_template.html",  # HTML email template
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")