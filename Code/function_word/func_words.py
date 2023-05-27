import os
import csv
from unidecode import unidecode

# Chemin vers le fichier des mots de fonction
function_words_file = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/function_word/function_words.txt"

# Chemin vers le dossier contenant les fichiers prétraités de Molière
moliere_dir = "Code/function_word/Fichier_Moliere"

# Chargement des mots de fonction
function_words = []
with open(function_words_file, "r", encoding="utf-8") as f:
    function_words = [word.strip() for word in f.readlines()]

# Liste pour stocker les résultats
results = []
results.append(["function_word"] + os.listdir(moliere_dir))

# Parcours des fichiers prétraités de Molière
for word in function_words:
    word_counts = [word]
    for filename in os.listdir(moliere_dir):
        file_path = os.path.join(moliere_dir, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="ISO-8859-1") as f:
                text = f.read()
                count = text.lower().split().count(unidecode(word.lower()))
                word_counts.append(str(count))
    results.append(word_counts)

# Écriture des résultats dans un fichier CSV
output_file = "resultats.csv"
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)

print("Le fichier CSV des résultats a été créé avec succès.")
