import os
import shutil

def move_files_by_extension(src_dir):
    # Dossiers de destination pour les fichiers .CR2 et .JPG
    cr2_dir = os.path.join(src_dir, 'CR2')
    jpg_dir = os.path.join(src_dir, 'JPG')

    # Création des dossiers CR2 et JPG s'ils n'existent pas
    if not os.path.exists(cr2_dir):
        os.makedirs(cr2_dir)
        print(f"Dossier créé : {cr2_dir}")
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir)
        print(f"Dossier créé : {jpg_dir}")

    # Boucle à travers les fichiers dans le répertoire source
    for filename in os.listdir(src_dir):
        # Récupération du chemin complet du fichier
        file_path = os.path.join(src_dir, filename)

        # Vérification si c'est bien un fichier
        if os.path.isfile(file_path):
            # Vérification de l'extension et déplacement
            if filename.lower().endswith('.cr2'):
                shutil.move(file_path, os.path.join(cr2_dir, filename))
                print(f"Déplacé : {filename} -> {cr2_dir}")
            elif filename.lower().endswith('.jpg'):
                shutil.move(file_path, os.path.join(jpg_dir, filename))
                print(f"Déplacé : {filename} -> {jpg_dir}")

if __name__ == "__main__":
    # Demander le chemin du répertoire source à l'utilisateur
    src_directory = input("Veuillez entrer le chemin du dossier contenant les fichiers CR2 et JPG : ")

    # Vérification que le dossier existe bien
    if os.path.exists(src_directory) and os.path.isdir(src_directory):
        move_files_by_extension(src_directory)
    else:
        print("Le chemin indiqué n'existe pas ou n'est pas un dossier valide.")
