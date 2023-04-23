import os
import glob
import string
import nltk
from nltk.corpus import stopwords
from ebooklib import epub
import ebooklib


def lecture_fichier(nom_fichier):
    livre = epub.read_epub(nom_fichier)
    texte = ''
    for item in livre.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            texte += item.get_content().decode('utf-8')
    return texte


def nettoyer(texte):
    # Convertir le texte en minuscule
    texte = texte.lower()

    # Supprimer la ponctuation
    texte = texte.translate(str.maketrans('', '', string.punctuation))

    # Tokenization
    tokens = nltk.word_tokenize(texte)

    # Suppression des stopwords
    stopwords_fr = set(stopwords.words('french'))
    tokens_filtrés = [mot for mot in tokens if mot.lower() not in stopwords_fr]

    texte_final = ' '.join(tokens_filtrés)

    return texte_final


def pretraitement_epub(dossier_entree, dossier_sortie):
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    for fichier_entree in glob.glob(os.path.join(dossier_entree, '*.epub')):
        # Lecture du contenu du fichier
        texte = lecture_fichier(fichier_entree)

        texte_nettoye = nettoyer(texte)

        nom_fichier_sortie = os.path.splitext(
            os.path.basename(fichier_entree))[0] + '.txt'
        chemin_fichier_sortie = os.path.join(
            dossier_sortie, nom_fichier_sortie)

        with open(chemin_fichier_sortie, 'w', encoding='utf-8') as f_sortie:
            f_sortie.write(texte_nettoye)


if __name__ == '__main__':

    dossier_entree = 'Code/Fichier_EPUB'
    dossier_sortie = 'Code/Fichier_text'

    pretraitement_epub(dossier_entree, dossier_sortie)
