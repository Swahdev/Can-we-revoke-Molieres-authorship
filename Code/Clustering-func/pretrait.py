import os
import re

def select_word_occurrences(folder_path, functional_words_file, output_folder):
    # Charger les mots fonctionnels à partir du fichier texte
    with open(functional_words_file, "r", encoding="utf-8") as f:
        functional_words = [word.strip() for word in f.readlines()]

    # Parcourir les fichiers dans le dossier
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                # Lire le contenu du fichier
                content = file.read().lower()

                # Extraire les occurrences des mots fonctionnels
                occurrences = []
                for word in functional_words:
                    # Traiter les cas spécifiques pour les chaînes de caractères avec apostrophe
                    if "'" in word:
                        # Utiliser une recherche régulière avec des alternatives pour inclure les cas spécifiques
                        pattern = re.compile(r"\b" + re.escape(word) + r"\b|\b" + re.escape(word.replace("'", "")) + r"\b")
                    else:
                        pattern = re.compile(r"\b" + re.escape(word) + r"\b")

                    matches = re.findall(pattern, content)
                    occurrences.extend(matches)

                # Enregistrer les occurrences dans un fichier texte avec le même nom
                output_file_path = os.path.join(output_folder, filename)
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.write("\n".join(occurrences))

# Chemin du dossier contenant les fichiers texte
text_folder = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/function_word/Fichier_Moliere"

# Chemin vers le fichier contenant les mots fonctionnels
functional_words_file = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/function_word/function_words.txt"

# Chemin du dossier de sortie pour les fichiers contenant les occurrences
output_folder = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Clustering-func/Fichiers_Moliere"

# Sélectionner les occurrences des mots fonctionnels dans les fichiers texte
select_word_occurrences(text_folder, functional_words_file, output_folder)
