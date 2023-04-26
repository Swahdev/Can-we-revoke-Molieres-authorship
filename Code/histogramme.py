import os
from os import path
import nltk
import matplotlib.pyplot as plt


def main():
    corpus_dir = "Code/Fichiers_Pretraitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    corpus_text = ""
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", encoding="utf-8") as file:
            corpus_text += file.read()
    tokens = nltk.word_tokenize(corpus_text)

    # Generate frequency distribution of words
    freq_dist = nltk.FreqDist(tokens)

    # Get top 100 words
    top_words = [word[0] for word in freq_dist.most_common(103)]
    top_words.remove("monsieur")
    top_words.remove("pourceaugnac")
    top_words.remove("jourdain")

    # Get frequency of top 100 words
    word_freq = [freq_dist[word] for word in top_words]

    # Plot histogram
    plt.figure(figsize=(20, 10))
    plt.bar(top_words, word_freq)
    plt.xticks(rotation=90)
    plt.xlabel("Mots")
    plt.ylabel("Fréquence")
    plt.title(
        "Histogramme de la fréquence des mots dans le corpus de Molière (sans 'monsieur')")
    plt.show()


if __name__ == '__main__':
    main()
