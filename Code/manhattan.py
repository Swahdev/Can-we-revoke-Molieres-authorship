import fasttext
import fasttext.util
import numpy as np
import os
from os import path


def main():
    # Charger le modèle FastText French
    ft = fasttext.load_model("Code/cc.fr.300.bin")

    # Chargement des textes de Corneille prétraités
    corpus_dir = "Code/Corneille-pre-traitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Calcul des vecteurs de chaque texte de Corneille
    corpus_vectors = {}
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", 
                  encoding="utf-8") as file:
            corpus_text = file.read()
            tokens = corpus_text.split()
            vectors = []
            for token in tokens:
                vector = ft.get_word_vector(token)
                vectors.append(vector)
            if vectors:
                corpus_vectors[file_name] = np.mean(vectors, axis=0)

    # Chargement des textes de Molière prétraités
    corpus_dir = "Code/Fichiers_Pretraitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Calcul des vecteurs de chaque texte de Molière et comparaison avec les
    # vecteurs de chaque texte de Corneille
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", 
                  encoding="utf-8") as file:
            corpus_text = file.read()
            tokens = corpus_text.split()
            vectors = []
            for token in tokens:
                vector = ft.get_word_vector(token)
                vectors.append(vector)
            if vectors:
                text_vector = np.mean(vectors, axis=0)
                for corneille_file, corneille_vector in corpus_vectors.items():
                    distance = np.sum(np.abs(text_vector - corneille_vector))
                    print(f"{file_name} {corneille_file} {distance}")


if __name__ == '__main__':
    main()
