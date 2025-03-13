import os

downloads_file=os.path.join(os.path.expanduser("~"),"Downloads")
downloads_manager=os.path.join(downloads_file,"İndirilenler Düzenleyicisi")

file_extensions ={
    "Resimler": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videolar": [".mp4", ".mkv", ".mov", ".avi", ".flv"],
    "Belgeler": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Ses Dosyaları": [".mp3", ".wav", ".ogg", ".flac"],
    "Arşivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Kurulum Dosyaları":[".exe", ".msi"],
    "Excel Dosyaları":[".csv", ".xlsx"],
    "Diğer": [] 
}

