import subprocess

scripts = [
    "organize_images.py",
    "organize_videos.py",
    "organize_documents.py",
    "organize_music.py",
    "organize_archives.py",
    "organize_setup.py",
    "organize_excel.py",
    "organize_other.py"
    
]

print("📂 Dosya düzenleme başlatılıyor...\n")

for script in scripts:
    print(f"➡ {script} çalıştırılıyor...")
    subprocess.run(["python", script])

print("\n✅ Tüm dosyalar organize edildi!")
input('Please press a any key...')