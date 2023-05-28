import os
import gensim
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_distances
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Chemin vers le répertoire contenant les fichiers texte lemmatisés de Molière
repertoire_moliere = "Code/Clustering/Fichiers_pretraite"

# Chemin vers le répertoire contenant les fichiers texte lemmatisés de Corneille
repertoire_corneille = "Code/Clustering/Corneille_pretraite"

# Liste pour stocker les documents de Molière
documents_moliere = []

# Parcours de tous les fichiers de Molière dans le répertoire
for nom_fichier in os.listdir(repertoire_moliere):
    chemin_fichier = os.path.join(repertoire_moliere, nom_fichier)

    if os.path.isfile(chemin_fichier) and nom_fichier.endswith(".txt"):
        # Lecture du fichier
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()

        # Ajout du contenu du fichier à la liste des documents de Molière
        documents_moliere.append(contenu)

# Liste pour stocker les documents de Corneille
documents_corneille = []

# Parcours de tous les fichiers de Corneille dans le répertoire
for nom_fichier in os.listdir(repertoire_corneille):
    chemin_fichier = os.path.join(repertoire_corneille, nom_fichier)

    if os.path.isfile(chemin_fichier) and nom_fichier.endswith(".txt"):
        # Lecture du fichier
        with open(chemin_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.read()

        # Ajout du contenu du fichier à la liste des documents de Corneille
        documents_corneille.append(contenu)

# Concaténation des documents de Molière et de Corneille
documents = documents_moliere + documents_corneille

# Chargement du modèle FastText pré-entraîné
modele_fasttext = gensim.models.FastText.load_fasttext_format(
    'Code/cc.fr.300.bin')

# Liste pour stocker les vecteurs de documents
vecteurs_documents = []

# Conversion des documents en vecteurs
for document in documents:
    # Tokenisation (séparation en mots)
    mots = document.split()

    # Conversion des mots en vecteurs FastText
    vecteurs_mots = [modele_fasttext.wv[mot]
                     for mot in mots if mot in modele_fasttext.wv]

    # Agrégation des vecteurs de mots pour obtenir un vecteur de document
    if vecteurs_mots:
        vecteur_document = sum(vecteurs_mots) / len(vecteurs_mots)
    else:
        # Si le document est vide, attribuer un vecteur nul
        vecteur_document = [0] * modele_fasttext.vector_size

    # Ajout du vecteur de document à la liste
    vecteurs_documents.append(vecteur_document)

# Utilisation des vecteurs de documents pour le clustering
# Nombre de clusters souhaité
nb_clusters = 5

# Calcul de la matrice de distance cosinus
distances_cosinus = cosine_distances(vecteurs_documents)

# Conversion de la matrice de distance en matrice de similarité
similarites = 1 - distances_cosinus

# Calcul de la matrice de lien
lien = sch.linkage(similarites, method='complete')

# Génération du dendrogramme
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(lien,
                            labels=[f.replace('.txt', '') for f in os.listdir(repertoire_moliere)] + [f.replace('.txt', '') for f in os.listdir(repertoire_corneille)])
plt.xlabel('Documents')
plt.ylabel('Distance')
plt.title('Dendrogramme')
# Rotation des étiquettes de l'axe x pour une meilleure lisibilité
plt.xticks(rotation=90)
plt.tight_layout()  # Ajustement automatique des marges
# Enregistrement de l'image en haute résolution
plt.savefig('dendrogramme.png', dpi=600)

# Initialisation de l'algorithme de clustering
kmeans = KMeans(n_clusters=nb_clusters, random_state=42)

# Application de l'algorithme de clustering sur les vecteurs de documents
kmeans.fit(vecteurs_documents)

# Obtention des labels de cluster attribués aux documents
labels_clusters = kmeans.labels_

# Enregistrement des résultats dans un fichier
resultats = []
for i, label in enumerate(labels_clusters):
    nom_fichier = os.listdir(repertoire_moliere)[i] if i < len(os.listdir(
        repertoire_moliere)) else os.listdir(repertoire_corneille)[i - len(os.listdir(repertoire_moliere))]
    nom_fichier_sans_ext = os.path.splitext(nom_fichier)[0]
    resultats.append(
        f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

with open('resultats.txt', 'w', encoding='utf-8') as fichier_resultats:
    fichier_resultats.write('\n'.join(resultats))

# Affichage des résultats
for resultat in resultats:
    print(resultat)
