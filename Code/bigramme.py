import os
from os import path
import nltk
from nltk.corpus import stopwords


def main():

    # Path to corpus directory
    corpus_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement"

    # Get list of all corpus files
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Read in corpus text from all files
    corpus_text = ""
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", encoding="utf-8") as file:
            corpus_text += file.read()

    # Tokenize the corpus text
    tokens = nltk.word_tokenize(corpus_text, language="french")

    # Remove stopwords from the tokenized corpus
    french_stopwords = stopwords.words('french')
    tokens = [token.lower() for token in tokens if token.isalpha()
              and token.lower() not in french_stopwords]

    # Generate bigrams and filter out unwanted bigrams
    bigrams = nltk.bigrams(tokens)
    filtered_bigrams = [bigram for bigram in bigrams if "jourdain"
                        not in bigram and "sotenville" not in bigram
                        and "pourceaugnac" not in bigram and bigram != (
                            "monsieur", "monsieur")
                        and bigram != ("plus", "plus")]

    # count frequency of bigrams
    freq_dist = nltk.FreqDist(filtered_bigrams)

    # Print the 20 most common bigrams
    for bigram, freq in freq_dist.most_common(25):
        print(bigram, freq)


if __name__ == '__main__':
    main()
