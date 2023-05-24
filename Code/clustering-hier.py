import os
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import fasttext

# Chemins vers les dossiers contenant les fichiers de chaque auteur
corneille_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Corneille-pre-traitement"
moliere_dir = "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/Fichiers_Pretraitement"

# Charger le modèle FastText French
ft = fasttext.load_model(
    "/Users/charleschikhani/Documents/L3/S6/Can-we-revoke-Molieres-authorship/Code/cc.fr.300.bin")

# Chargement des textes de Corneille prétraités
corneille_files = [os.path.join(corneille_dir, f) for f in os.listdir(
    corneille_dir) if f.endswith(".txt")]

# Chargement des textes de Molière prétraités
moliere_files = [os.path.join(moliere_dir, f)
                 for f in os.listdir(moliere_dir) if f.endswith(".txt")]

# Fonction pour obtenir les vecteurs de chaque texte


def get_text_vectors(files):
    vectors = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()
            tokens = text.split()
            text_vector = np.mean([ft.get_word_vector(token)
                                  for token in tokens], axis=0)
            vectors.append(text_vector)
    return np.array(vectors)


# Obtenir les vecteurs de chaque texte de chaque auteur
corneille_vectors = get_text_vectors(corneille_files)
moliere_vectors = get_text_vectors(moliere_files)

# Concaténer les vecteurs des deux auteurs pour effectuer le clustering
all_vectors = np.concatenate([corneille_vectors, moliere_vectors], axis=0)

# Effectuer le clustering hiérarchique
clustering = AgglomerativeClustering(
    n_clusters=3, metric="euclidean", linkage="ward")
clusters = clustering.fit_predict(all_vectors)

# Afficher les résultats du clustering pour chaque fichier
for i in range(len(clusters)):
    file_name = os.path.basename(corneille_files[i]) if i < len(
        corneille_files) else os.path.basename(moliere_files[i-len(corneille_files)])
    print(f"{file_name}: Cluster {clusters[i]}")

# Afficher le dendrogramme
Z = linkage(all_vectors, 'ward')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z, labels=[os.path.basename(
    file) for file in corneille_files] + [os.path.basename(file) for file in moliere_files])
plt.show()
