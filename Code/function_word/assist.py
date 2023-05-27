import os
import csv
import re

def count_word_occurrences(folder_path, words):
    # Initialiser un dictionnaire pour stocker les occurrences des mots
    word_counts = {word: [word] for word in words}

    # Parcourir les fichiers dans le dossier
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                # Lire le contenu du fichier
                content = file.read().lower()

                # Parcourir les mots dans le contenu
                for word in words:
                    # Utiliser des expressions régulières pour trouver les occurrences du mot dans le contenu
                    pattern = re.compile(r"\b" + re.escape(word) + r"\b")
                    count = len(re.findall(pattern, content))

                    # Ajouter le nombre d'occurrences du mot à la liste correspondante dans le dictionnaire
                    word_counts[word].append(count)

    return word_counts

# Liste des mots à compter
words_to_count = ["déjà", "êtes", "était", "-là", "être", "qu'"]

# Chemin du dossier contenant les fichiers texte
text_folder = "Code/function_word/Fichier_Moliere"

# Compter les occurrences des mots dans les fichiers texte
word_occurrences = count_word_occurrences(text_folder, words_to_count)

# Chemin du fichier CSV de sortie
output_csv = "word_occurrences.csv"

# Écrire les résultats dans le fichier CSV
with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["function_word"] + os.listdir(text_folder))
    for word in words_to_count:
        writer.writerow(word_occurrences[word])