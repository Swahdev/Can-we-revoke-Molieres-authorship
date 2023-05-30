import os
from os import path
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def main():
    corpus_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement"
    corpus_files = [f for f in os.listdir(corpus_dir) if f.endswith(".txt")]

    # Concatenation du text

    corpus_text = ""
    for file_name in corpus_files:
        with open(path.join(corpus_dir, file_name), "r", encoding="utf-8") as file:
            corpus_text += file.read()

    options = {
        "background_color": "white",
        "width": 2000,
        "height": 1000,
        "max_words": 2000,
        "max_font_size": 150,
        "prefer_horizontal": 1.0,
        # liste de stopwords à supprimer
        "stopwords": ["pourceaugnac", "jourdain"]
    }

    # Generate a word cloud image

    wordcloud = WordCloud(**options).generate(corpus_text)

    # Display the generated image

    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    # plt.show()
    plt.savefig("nuage_de_mots.png", dpi=600, bbox_inches='tight')


if __name__ == '__main__':
    main()
