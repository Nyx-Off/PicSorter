# PicSorter
![Static Badge](https://img.shields.io/badge/Contributeur-1-brightgreen?style=flat&logo=clubhouse&logoColor=white&logoSize=auto) 
![License](https://img.shields.io/github/license/Nyx-Off/AceVenturaTheGame) 
![Static Badge](https://img.shields.io/badge/Python-black?style=plastic&logo=python&logoColor=white&logoSize=auto&color=yellow)


**PicSorter** est un outil Python conçu pour organiser automatiquement les fichiers `.CR2` et `.JPG` en les déplaçant dans des dossiers distincts. Si vous êtes comme moi et utilisez un appareil photo Canon qui génère ces deux types de fichiers, PicSorter vous aidera à maintenir vos fichiers bien organisés après chaque session photo.

## Mon Expérience et Pourquoi j'ai Créé **PicSorter**

En tant que photographe amateur utilisant un appareil Canon, chaque fois que je prends des photos, deux types de fichiers sont générés : des fichiers **CR2** (RAW) et des **JPG**. Ces fichiers se retrouvent mélangés dans le même dossier, ce qui peut vite devenir encombrant. 

Je devais auparavant les trier manuellement, ce qui prenait du temps et devenait une tâche répétitive. C’est pourquoi j’ai créé **PicSorter**. Ce programme simple permet de trier automatiquement les fichiers **CR2** et **JPG** en les déplaçant dans des dossiers séparés, créant ainsi une organisation propre et fonctionnelle.

Grâce à **PicSorter**, je peux maintenant me concentrer sur l'essentiel : la retouche de mes photos et la création, sans perdre de temps à trier manuellement mes fichiers.

## Fonctionnalités
- Trie automatique des fichiers **.CR2** et **.JPG** dans des dossiers distincts.
- Création des dossiers **CR2** et **JPG** s'ils n'existent pas encore.
- Déplacement des fichiers (pas de simple copie), maintenant votre répertoire de travail propre.

## Prérequis
- Python 3.x

## Installation
1. Clonez ce dépôt GitHub :
    ```bash
    git clone https://github.com/votreutilisateur/PicSorter.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd PicSorter
    ```

3. Exécutez le script :
    ```bash
    python pic_sorter.py
    ```

## Utilisation
1. Lancez le script. Celui-ci vous demandera d'entrer le chemin du dossier contenant vos fichiers **CR2** et **JPG**.
2. Le programme créera automatiquement deux dossiers, **CR2** et **JPG**, dans le répertoire spécifié (s'ils n'existent pas encore).
3. Les fichiers **.CR2** seront déplacés dans le dossier **CR2** et les fichiers **.JPG** dans le dossier **JPG**.

## Exemple
```bash
Veuillez entrer le chemin du dossier contenant vos fichiers CR2 et JPG : /chemin/vers/votre/dossier
Dossier créé : /chemin/vers/votre/dossier/CR2
Dossier créé : /chemin/vers/votre/dossier/JPG
Déplacé : photo1.CR2 -> /chemin/vers/votre/dossier/CR2
Déplacé : photo1.JPG -> /chemin/vers/votre/dossier/JPG
```

## Contribuer
Si vous avez des suggestions, des améliorations ou si vous trouvez des bugs, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.
