import os
import numpy as np
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.cluster import AgglomerativeClustering

# Chemin vers le répertoire contenant les fichiers texte lemmatisés de Molière et Corneille
repertoire_moliere = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Clustering/Fichiers_pretraite"
repertoire_corneille = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Clustering/Corneille_pretraite"

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

# Vectorisation des documents en utilisant la représentation binaire (0 ou 1)
vectoriseur = CountVectorizer(binary=True)
matrice_documents = vectoriseur.fit_transform(documents)

# Conversion de la matrice creuse en matrice dense
matrice_documents_dense = matrice_documents.toarray()

# Calcul de la similarité de Jaccard entre les documents
similarite_jaccard = pairwise_distances(matrice_documents_dense, metric="jaccard")

# Algorithme de clustering hiérarchique agglomératif
agglomeratif = AgglomerativeClustering(n_clusters=None, distance_threshold=0, linkage="average", affinity="precomputed")
agglomeratif.fit(similarite_jaccard)

# Obtention des labels de cluster attribués aux documents
labels_clusters = agglomeratif.labels_

# Génération du dendrogramme
dendrogramme = sch.dendrogram(sch.linkage(similarite_jaccard, method="average"), labels=[f.replace('.txt', '') for f in os.listdir(repertoire_moliere)] + [f.replace('.txt', '') for f in os.listdir(repertoire_corneille)])

# Enregistrement des résultats dans un fichier
resultats = []
for i, label in enumerate(labels_clusters):
    nom_fichier = os.listdir(repertoire_moliere)[i] if i < len(os.listdir(repertoire_moliere)) else os.listdir(repertoire_corneille)[i - len(os.listdir(repertoire_moliere))]
    nom_fichier_sans_ext = nom_fichier.replace('.txt', '')
    resultats.append(f"Document {i+1}: {nom_fichier_sans_ext}, Cluster {label}")

with open('resultats_jacard.txt', 'w', encoding='utf-8') as fichier_resultats:
    fichier_resultats.write('\n'.join(resultats))

# Affichage des résultats
for resultat in resultats:
    print(resultat)

# Affichage du dendrogramme
plt.xlabel('Documents')
plt.ylabel('Distance')
plt.title('Dendrogramme')

# Ajustement de la taille de la figure
fig = plt.gcf()
fig.set_size_inches(17, 12)

plt.savefig('dendrogramme.png', dpi=600)
plt.show()
