import os
import numpy as np


def main():
    # Chargement des textes de Corneille prétraités
    corpus_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Calcul des ensembles de tokens de chaque texte de Corneille
    corpus_token_sets = {}
    for file_name in corpus_files:
        with open(os.path.join(corpus_dir, file_name), "r",
                  encoding="utf-8") as file:
            corpus_text = file.read()
            tokens = set(corpus_text.split())
            if tokens:
                corpus_token_sets[file_name] = tokens

    # Chargement des textes de Molière prétraités
    corpus_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Fichiers_Pretraitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Calcul des ensembles de tokens de chaque texte de Molière et comparaison
    # avec les ensembles de tokens de chaque texte de Corneille
    for file_name in corpus_files:
        with open(os.path.join(corpus_dir, file_name), "r",
                  encoding="utf-8") as file:
            corpus_text = file.read()
            tokens = set(corpus_text.split())
            if tokens:
                text_token_set = tokens
                for corneille_file, corneille_token_set in corpus_token_sets.items():
                    jaccard_distance = (1 -
                                        len(text_token_set.intersection(
                                            corneille_token_set))
                                        / len(text_token_set.union(
                                            corneille_token_set)))
                    print(f"{file_name} vs {corneille_file}: {jaccard_distance}")


if __name__ == '__main__':
    main()
