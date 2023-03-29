import nltk
import os
import glob
import re
from nltk.tokenize import TweetTokenizer, word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
stopwords_fr = set(stopwords.words('french'))

tokenizer = TweetTokenizer(
    preserve_case=False, reduce_len=True, strip_handles=True)
stemmer = SnowballStemmer('french')

mots_a_supprimer = ['html', 'http', 'xml', 'fr',
                    'teihead', 'filedesc', 'titlestmt', 'titl']


def pretraitement(texte):
    # Suppression des balises XML
    texte = re.sub('<[^<]+>', '', texte)
    # Tokenisation des phrases
    phrases = nltk.sent_tokenize(texte, language='french')
    # Tokenisation des mots et suppression des mots non français, les stopwords et les mots à supprimer
    mots = []
    for phrase in phrases:
        tokens = tokenizer.tokenize(phrase)
        for token in tokens:
            if token.isalpha() and token.lower() not in stopwords_fr and token.lower() not in mots_a_supprimer:
                mots.append(stemmer.stem(token.lower()))
    return mots


if __name__ == '__main__':
    # Récupération des fichiers à prétraiter
    dossier_xml = 'Fichier_XML'
    dossier_sortie = 'Fichiers_Pretraitement'
    # Recherche de tous les fichiers XML dans le dossier d'entrée
    fichiers_entree = glob.glob(os.path.join(dossier_xml, '*.xml'))
    # Boucle sur tous les fichiers XML trouvés
    for fichier_entree in fichiers_entree:
        # Construire le nom de fichier de sortie en remplaçant l'extension
        # ".xml" par ".txt"
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
