import os
import shutil
from config import downloads_file, downloads_manager, file_extensions

def move_other_files():
    os.makedirs(downloads_manager, exist_ok=True)  # Ana düzenleyici klasörü oluştur
    other_folder = os.path.join(downloads_manager, "Diğer")
    os.makedirs(other_folder, exist_ok=True)

    known_extensions = [ext for ext_list in file_extensions.values() for ext in ext_list]

    for file in os.listdir(downloads_file):
        file_path = os.path.join(downloads_file, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            if ext.lower() not in known_extensions:
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Taşındı: {file} -> Diğer")

move_other_files()