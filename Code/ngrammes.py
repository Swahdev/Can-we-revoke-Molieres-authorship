import os
import glob
import string
import nltk
from nltk.util import ngrams
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def ngrammes(texte, n):
    # Création des n-grammes
    ngrammes = []
    for i in range(len(texte)-n+1):
        ngramme = texte[i:i+n]
        ngrammes.append(ngramme)
    return ngrammes


def construction_graphes(fichier_entre, n):
    compteur = Counter()
    for fichier_entre in fichier_entre:
        with open(fichier_entre, 'r') as f_entree:
            texte = f_entree.read()
            ngrammes = ngrams(texte, n)
            compteur.update(ngrammes)
    # Création du graphe
    G = nx.Graph()
    for ngramme, poids in compteur.items():
        G.add_node(ngramme, weight=poids)  # Modification de poids en weight
    # Calcul des poids des arêtes
    for u, v in nx.non_edges(G):
        poids_u = G.nodes[u]['weight']
        poids_v = G.nodes[v]['weight']
        intersection = len(set(u).intersection(v))
        similarite = intersection / (n - 1)  # Similarité de Jaccard
        poids_arete = poids_u + poids_v - 2 * \
            poids_u * poids_v * (1 - similarite)
        G.add_edge(u, v, weight=poids_arete)
    return G


if __name__ == '__main__':
    dossier = 'Fichiers_Pretraitement'
    fichier_entre = glob.glob(os.path.join(dossier, '*.txt'))

    # Construction du graphe 4-grammes
    n = 4
    G = construction_graphes(fichier_entre, n)

    # Affichage du graphe
    pos = nx.spring_layout(G, k=0.1, iterations=50)
    weights = [G[u][v]['weight'] for u, v in G.edges]
    nx.draw(G, pos, node_color='#A0CBE2', width=weights,
            edge_color=weights, edge_cmap=plt.cm.Blues, with_labels=True)
    plt.show()
