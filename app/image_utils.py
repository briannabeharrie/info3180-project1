import os

def get_uploaded_images(upload_folder):
    return [file for _, _, files in os.walk(upload_folder) for file in files]