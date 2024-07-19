import os
from PIL import Image, UnidentifiedImageError

# Pfad zum Ordner mit den Bildern
folder_path = r'C:\Users\ellys\OneDrive\Soso\Schule\Bionik\Seminararbeit\knn\PetImages\Cat'

# Durchlaufe alle Dateien im Ordner
for filename in os.listdir(folder_path):
    # Prüfe, ob die Datei eine .jpeg-Datei ist
    if filename.endswith('.jpeg'):
        # Voller Pfad zur Datei
        file_path = os.path.join(folder_path, filename)
        
        try:
            # Öffne das Bild
            with Image.open(file_path) as img:
                # Konvertiere das Bild in den RGB-Modus, falls nötig
                if img.mode in ('P', 'RGBA'):
                    img = img.convert('RGB')
                
                # Entferne die .jpeg-Endung und füge .jpg hinzu
                new_filename = filename.replace('.jpeg', '.jpg')
                new_file_path = os.path.join(folder_path, new_filename)
                
                # Speichere das Bild mit der neuen Endung
                img.save(new_file_path, 'JPEG')
                
            # Optional: Lösche die alte .jpeg-Datei
            os.remove(file_path)
        
        except UnidentifiedImageError:
            print(f"Datei '{filename}' konnte nicht als Bild erkannt werden.")
            continue

print('Konvertierung abgeschlossen!')
