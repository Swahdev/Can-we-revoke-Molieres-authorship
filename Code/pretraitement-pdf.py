import fitz
import os
import glob
import re
import langdetect
from nltk.tokenize import TweetTokenizer, word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
nltk.download('punkt')
stopwords_fr = set(stopwords.words('french'))

tokenizer = TweetTokenizer(
    preserve_case=False, reduce_len=True, strip_handles=True)
stemmer = SnowballStemmer('french')

mots_a_supprimer = ['html', 'http', 'xml', 'fr',
                    'teihead', 'filedesc', 'titlestmt', 'titl', 'informatique', 'moliere_amants', 'molière']


def pretraitement(texte):
    # Suppression des balises XML
    texte = re.sub('<[^<]+>', '', texte)
    # Extraction de tous les mots en minuscules
    mots = word_tokenize(texte.lower(), language='french')
    # Suppression des mots non français, des stopwords et des mots à supprimer
    mots_filtres = []
    for mot in mots:
        # Conserver les mots contenant des tirets ou des apostrophes
        if mot not in stopwords_fr and mot not in mots_a_supprimer:
            try:
                # Vérification que le mot est en français
                if langdetect.detect(mot) == 'fr':
                    mots_filtres.append(mot)
            except:
                pass
    return mots_filtres


if __name__ == '__main__':
    # Récupération des fichiers à prétraiter
    dossier_pdf = '/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille'
    dossier_sortie = '/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement'
    # Recherche de tous les fichiers PDF dans le dossier d'entrée
    fichiers_entree = glob.glob(os.path.join(dossier_pdf, '*.pdf'))
    # Boucle sur tous les fichiers PDF trouvés
    for fichier_entree in fichiers_entree:
        # Construire le nom de fichier de sortie en remplaçant l'extension
        # ".pdf" par ".txt"
        nom_fichier_sortie = os.path.splitext(
            os.path.basename(fichier_entree))[0] + '.txt'
        chemin_fichier_sortie = os.path.join(
            dossier_sortie, nom_fichier_sortie)
        # Ouverture du fichier PDF avec fitz
        with fitz.open(fichier_entree) as doc:
            # Boucle sur toutes les pages du fichier PDF
            mots_stem = []
            for page in doc:
                # Extraction du texte de la page
                texte = page.get_text()
                # Appel de la fonction de prétraitement
                mots_stem += pretraitement(texte)
        # Écriture des résultats dans le fichier de sortie
        with open(chemin_fichier_sortie, 'w') as f_sortie:
            f_sortie.write('\n'.join(mots_stem))
            print(
                f"Les résultats du prétraitement ont été enregistrés dans le fichier {chemin_fichier_sortie}.")
