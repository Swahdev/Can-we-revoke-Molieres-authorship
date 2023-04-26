Très bien. Pour poursuivre votre analyse, vous pouvez maintenant effectuer les étapes suivantes :

1. Charger les textes du corpus de Corneille pré-traités dans une liste de textes.
2. Charger les textes du corpus de Molière pré-traités dans une autre liste de textes.
3. Pour chaque texte de Corneille, calculer la similarité avec chaque texte de Molière en utilisant le modèle de plongement FastText.
4. Afficher les résultats de similarité pour chaque paire de textes.

Voici un exemple de code pour les étapes 1 et 2 :

```python
import os
from gensim.utils import simple_preprocess

# Chargement des textes de Corneille
corneille_dir = "Pre-Traite_Corneille"
corneille_texts = []
for file_name in os.listdir(corneille_dir):
    with open(os.path.join(corneille_dir, file_name), "r", encoding="utf-8") as file:
        text = file.read()
        tokens = simple_preprocess(text)  # prétraitement avec gensim
        corneille_texts.append(tokens)

# Chargement des textes de Molière
moliere_dir = "Pre-Traite_Moliere"
moliere_texts = []
for file_name in os.listdir(moliere_dir):
    with open(os.path.join(moliere_dir, file_name), "r", encoding="utf-8") as file:
        text = file.read()
        tokens = simple_preprocess(text)  # prétraitement avec gensim
        moliere_texts.append(tokens)
```

Vous pouvez ensuite créer des boucles pour parcourir chaque paire de textes et calculer leur similarité :

```python
# Calcul des similarités
for i, corneille_text in enumerate(corneille_texts):
    for j, moliere_text in enumerate(moliere_texts):
        similarity = model.wv.n_similarity(corneille_text, moliere_text)
        print(f"Similarité entre le texte {i} de Corneille et le texte {j} de Molière : {similarity}")
```

Cette méthode peut être assez coûteuse en temps de calcul si vous avez beaucoup de textes à comparer, car elle calcule toutes les paires de similarités. Si vous avez des ressources limitées, vous pouvez envisager d'utiliser une méthode de recherche de similarité plus rapide, telle que la recherche de voisins les plus proches (k-NN) ou l'indexation de vecteurs.