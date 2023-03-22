from nltk.tokenize import word_tokenize
from nltk.stem.porter import FrenchStemmer
from nltk.corpus import stopwords
import nltk
import os
import glob

nltk.download('stopwords')


def pretraitement(texte):
    # Tokenisation des mots et suppression de la ponctuation
    tokens = word_tokenize(texte, language='french')
    mots = [token.lower() for token in tokens if token.isalpha()]

    # Suppression des stopwords
    stop_words = set(stopwords.words('french'))
    mots_sans_stopwords = [mot for mot in mots if mot not in stop_words]

    # Stemming des mots
    stemmer = FrenchStemmer()
    mots_stem = [stemmer.stem(mot) for mot in mots_sans_stopwords]

    return mots_stem


if __name__ == '__main__':
    # Récupération des fichiers à prétraiter
    dossier_xml = 'Code/Fichier_XML'
    dossier_sortie = 'Code/Fichiers_Pretraitement'
    # Recherche de tous les fichiers XML dans le dossier d'entrée
    fichiers_entree = glob.glob(os.path.join(dossier_xml, '*.xml'))
    # Boucle sur tous les fichiers XML trouvés
    for fichier_entree in fichiers_entree:
        # Construire le nom de fichier de sortie en remplaçant l'extension ".xml" par ".txt"
        nom_fichier_sortie = os.path.splitext(
            os.path.basename(fichier_entree))[0] + '.txt'
        chemin_fichier_sortie = os.path.join(
            dossier_sortie, nom_fichier_sortie)
        # Lecture du contenu du fichier
        with open(fichier_entree, 'r') as f_entree:
            texte = f_entree.read()
        # Appel de la fonction de prétraitement
        mots_stem = pretraitement(texte)
        # Écriture des résultats dans le fichier de sortie
        with open(chemin_fichier_sortie, 'w') as f_sortie:
            f_sortie.write('\n'.join(mots_stem))
            print(
                f"Les résultats du prétraitement ont été enregistrés dans le fichier {chemin_fichier_sortie}.")
