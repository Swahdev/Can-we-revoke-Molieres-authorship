import os
from os import path
import nltk
from nltk.corpus import stopwords


def main():
    corpus_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement"

    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    corpus_text = ""
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", encoding="utf-8") as file:
            corpus_text += file.read()

    tokens = nltk.word_tokenize(corpus_text, language="french")

    # Remove stopwords from the tokenized corpus
    french_stopwords = stopwords.words('french')

    tokens = [token.lower() for token in tokens if token.isalpha()
              and token.lower() not in french_stopwords]

    # Generate trigrams
    trigrams = nltk.trigrams(tokens)
    filtered_trigrams = [trigram for trigram in trigrams if "jourdain" not
                         in trigram and "sotenville" not in trigram and
                         "pourceaugnac" not in trigram and "croisy" not in
                         trigram and trigram != (
                             "monsieur", "monsieur", "monsieur") and
                         trigram != ("jourdain", "monsieur", "jourdain") and
                         trigram != ("monsieur", "jourdain", "monsieur") and
                         trigram != ("monsieur", "monsieur", "jourdain") and
                         trigram != ("amour", "amour", "amour") and
                         trigram != ("monsieur", "monsieur", "oui") and
                         trigram != ("plus", "plus", "plus") and
                         trigram != ('discours', 'trois', 'unités') and
                         trigram != ('toutes', 'éditions', 'publiées') and
                         trigram != ('histoires', 'livre', 'chapitre') and
                         trigram != ('œuvres', 'complètes', 'œuvres') and
                         trigram != ('complètes', 'œuvres', 'complètes') and
                         trigram != ('éditions', 'collationnées',
                                     'personnages')
                         and trigram != ('éditions', 'collationnées', 'éditions')
                         and trigram != ('collationnées', 'éditions', 'séparées')
                         and trigram != ('éditions', 'séparées', 'acteurs')
                         and trigram != ('extrait', 'éditions', 'collationnées')]

    # count frequency of trigrams
    freq_dist = nltk.FreqDist(filtered_trigrams)

    for trigram, freq in freq_dist.most_common(25):
        print(trigram, freq)


if __name__ == '__main__':
    main()
