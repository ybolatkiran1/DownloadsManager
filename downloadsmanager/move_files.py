import os
import shutil
from config import downloads_file, downloads_manager

def move_files(folder_name, extensions):
    """
    Verilen dosya uzantılarına sahip dosyaları belirlenen klasöre taşır.
    Eğer klasör yoksa oluşturur.
    """
    hedef_klasor = os.path.join(downloads_manager, folder_name)

    # 📂 Eğer klasör yoksa oluştur
    if not os.path.exists(hedef_klasor):
        os.makedirs(hedef_klasor)

    # 📂 İndirilenler klasöründeki dosyaları kontrol et
    for file in os.listdir(downloads_file):
        file_path = os.path.join(downloads_file, file)

        # 📂 Eğer bu bir dosya ise ve uzantısı eşleşiyorsa taşı
        if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, hedef_klasor)
            print(f"📂 {file} -> {hedef_klasor} klasörüne taşındı.")

