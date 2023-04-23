# Explications Brouilloin

Ces deux lignes de code calculent le poids d'une arête entre deux nœuds dans le
graphe de co-occurrence en utilisant la mesure de similarité de Jaccard.

La variable similarite représente la similarité de Jaccard entre deux n-grammes,
qui est le nombre d'éléments communs divisé par le nombre total d'éléments dans
les deux ensembles. Ici, intersection représente le nombre de co-occurrences
communes entre deux n-grammes et (n-1) représente le nombre total de
co-occurrences possibles pour deux n-grammes.

La variable poids_arete représente le poids de l'arête entre deux nœuds dans le
graphe de co-occurrence. Elle est calculée en utilisant les poids des deux nœuds
(c'est-à-dire le nombre de fois où chaque n-gramme apparaît dans le corpus) et
la mesure de similarité de Jaccard. Plus la similarité de Jaccard est grande,
plus le poids de l'arête est faible, ce qui signifie que les n-grammes sont
moins similaires.

La distance de Manhattan (également appelée distance L1) est une mesure de
distance qui calcule la somme des différences absolues entre les coordonnées des
deux points dans un espace vectoriel. Elle est ainsi nommée car elle mesure la
distance entre deux points en se déplaçant sur un quadrillage comme si on
circulait dans les rues d'un plan de la ville de Manhattan.

En comparaison, la distance euclidienne (également appelée distance L2) est
calculée en prenant la racine carrée de la somme des carrés des différences
entre les coordonnées des deux points. Elle mesure la distance entre deux points
dans un espace en ligne droite.

En résumé, la distance de Manhattan considère les déplacements en ligne droite
horizontale ou verticale, tandis que la distance euclidienne mesure la distance
en ligne droite à vol d'oiseau.

Il est tout à fait possible d'utiliser la distance de Manhattan dans un modèle,
en particulier pour mesurer la similarité entre deux vecteurs. Cependant, pour
notre cas spécifique de recherche de paternité de texte, la distance de
Manhattan ne semble pas être la meilleure option car elle ne prend pas en compte
la direction ou l'orientation des vecteurs et ne mesure que la distance entre
les valeurs numériques des dimensions des vecteurs. En revanche, la distance
cosinus est plus adaptée pour notre cas car elle mesure la similarité en termes
de direction ou d'orientation des vecteurs, ce qui est important pour les
représentations vectorielles de texte.

Non utilisation de la méthode "Bag-of-Words".
La modification que vous proposez ne remplace pas les lignes de construction du
graphe par quelque chose de plus efficace, mais par une autre méthode
d'extraction de caractéristiques appelée "Bag-of-Words". Cette méthode consiste
à extraire toutes les séquences de mots de longueurs comprises entre
ngram_range[0] et ngram_range[1], puis à construire un dictionnaire de
max_features mots les plus fréquents, qui serviront de caractéristiques pour
représenter chaque document en tant que vecteur.

Cela peut être efficace dans certains cas, mais cela dépend du domaine
d'application et de la nature des données. Dans le cas de la recherche de la
paternité des textes de Molière, il est possible que les caractéristiques
extraites à partir des n-grammes soient plus pertinentes pour la tâche que
celles extraites à partir du Bag-of-Words.

Cependant, si vous souhaitez essayer la méthode du Bag-of-Words, voici comment
vous pouvez le faire en utilisant la bibliothèque scikit-learn :
