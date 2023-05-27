import nltk
import os
import glob
import re
import langdetect
from nltk.tokenize import TweetTokenizer

nltk.download('punkt')

tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)

mots_a_supprimer = ['html', 'http', 'xml', 'fr',
                    'teihead', 'filedesc', 'titlestmt', 'titl', 'informatique', 'moliere_amants', 'molière', '.', ',']
mots_a_inclure = ['déjà', 'jusqu\'', 'êtes', 'était', 'après','-là', 'là', 'où', '-même', 'même', 's\'', 'c\'', 'à','n\'']

def pretraitement(texte):
    # Suppression des balises XML
    texte = re.sub('<[^<]+>', '', texte)
    # Tokenisation des mots
    mots = tokenizer.tokenize(texte.lower())
    # Suppression des mots non français et des mots à supprimer
    mots_filtres = []
    for mot in mots:
        # Conserver les mots contenant des tirets ou des apostrophes
        if '-' in mot or "'" in mot or mot not in mots_a_supprimer or mot in mots_a_inclure:
            mots_filtres.append(mot)
        else:
            try:
                # Vérification que le mot est en français
                if langdetect.detect(mot) == 'fr':
                    mots_filtres.append(mot)
            except:
                pass
    return mots_filtres


if __name__ == '__main__':
    # Récupération des fichiers à prétraiter
    dossier_xml = '/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Fichier_XML'
    dossier_sortie = '/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/function_word/Fichier_Moliere'
    # Recherche de tous les fichiers XML dans le dossier d'entrée
    fichiers_entree = glob.glob(os.path.join(dossier_xml, '*.xml'))
    # Boucle sur tous les fichiers XML trouvés
    for fichier_entree in fichiers_entree:
        # Construire le nom de fichier de sortie en remplaçant l'extension ".xml" par ".txt"
        nom_fichier_sortie = os.path.splitext(os.path.basename(fichier_entree))[0] + '.txt'
        chemin_fichier_sortie = os.path.join(dossier_sortie, nom_fichier_sortie)
        # Lecture du contenu du fichier
        with open(fichier_entree, 'r', encoding='utf-8') as f_entree:
            texte = f_entree.read()
        # Appel de la fonction de prétraitement
        mots_filtres = pretraitement(texte)
        # Écriture des résultats dans le fichier de sortie
        with open(chemin_fichier_sortie, 'w', encoding='utf-8') as f_sortie:
            f_sortie.write('\n'.join(mots_filtres))
        print(f"Les résultats du prétraitement ont été enregistrés dans le fichier {chemin_fichier_sortie}.")
