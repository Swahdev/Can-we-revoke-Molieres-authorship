import os
import gensim
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances
from sklearn.metrics import jaccard_score

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
modele_fasttext = gensim.models.FastText.load_fasttext_format('Code/cc.fr.300.bin')

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

# Algorithme de K-means
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(vecteurs_documents)
labels_kmeans = kmeans.labels_

# Distance euclidienne
distances_euclidienne = euclidean_distances(vecteurs_documents)
lien_euclidien = sch.linkage(distances_euclidienne, method='complete')
labels_euclidienne = sch.fcluster(lien_euclidien, t=5, criterion='maxclust')

# Similarité cosinus
similarite_cosinus = 1 - cosine_distances(vecteurs_documents)
distance_cosinus = 1 - similarite_cosinus
lien_cosinus = sch.linkage(distance_cosinus, method='complete')
labels_cosinus = sch.fcluster(lien_cosinus, t=5, criterion='maxclust')

# Similarité de Jaccard
vecteurs_binaires = [[1 if val > 0 else 0 for val in vecteur] for vecteur in vecteurs_documents]
distance_jaccard = 1 - jaccard_score(vecteurs_binaires, vecteurs_binaires, average='weighted')
lien_jaccard = sch.linkage(distance_jaccard, method='complete')
labels_jaccard = sch.fcluster(lien_jaccard, t=5, criterion='maxclust')

# Enregistrement des résultats dans des fichiers texte
resultats_kmeans = []
resultats_euclidienne = []
resultats_cosinus = []
resultats_jaccard = []

fichiers = os.listdir(repertoire_moliere) + os.listdir(repertoire_corneille)
for i, label in enumerate(labels_kmeans):
    nom_fichier = fichiers[i]
    nom_fichier_sans_ext = nom_fichier.replace('.txt', '')
    resultats_kmeans.append(f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

for i, label in enumerate(labels_euclidienne):
    nom_fichier = fichiers[i]
    nom_fichier_sans_ext = nom_fichier.replace('.txt', '')
    resultats_euclidienne.append(f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

for i, label in enumerate(labels_cosinus):
    nom_fichier = fichiers[i]
    nom_fichier_sans_ext = nom_fichier.replace('.txt', '')
    resultats_cosinus.append(f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

for i, label in enumerate(labels_jaccard):
    nom_fichier = fichiers[i]
    nom_fichier_sans_ext = nom_fichier.replace('.txt', '')
    resultats_jaccard.append(f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

with open('resultats_kmeans.txt', 'w', encoding='utf-8') as fichier_resultats_kmeans:
    fichier_resultats_kmeans.write('\n'.join(resultats_kmeans))

with open('resultats_euclidienne.txt', 'w', encoding='utf-8') as fichier_resultats_euclidienne:
    fichier_resultats_euclidienne.write('\n'.join(resultats_euclidienne))

with open('resultats_cosinus.txt', 'w', encoding='utf-8') as fichier_resultats_cosinus:
    fichier_resultats_cosinus.write('\n'.join(resultats_cosinus))

with open('resultats_jaccard.txt', 'w', encoding='utf-8') as fichier_resultats_jaccard:
    fichier_resultats_jaccard.write('\n'.join(resultats_jaccard))

# Affichage des dendrogrammes
plt.figure(figsize=(12, 8))

plt.subplot(221)
dendrogramme_kmeans = sch.dendrogram(lien_kmeans, labels=fichiers, orientation='left')
plt.title('Dendrogramme - K-means')

plt.subplot(222)
dendrogramme_euclidienne = sch.dendrogram(lien_euclidien, labels=fichiers, orientation='left')
plt.title('Dendrogramme - Distance Euclidienne')

plt.subplot(223)
dendrogramme_cosinus = sch.dendrogram(lien_cosinus, labels=fichiers, orientation='left')
plt.title('Dendrogramme - Similarité Cosinus')

plt.subplot(224)
dendrogramme_jaccard = sch.dendrogram(lien_jaccard, labels=fichiers, orientation='left')
plt.title('Dendrogramme - Similarité de Jaccard')

plt.tight_layout()
plt.show()
