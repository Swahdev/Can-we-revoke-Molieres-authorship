# Pour rapport

## Les étapes

Mesure de similarité : Vous devez choisir une mesure de similarité appropriée
pour comparer les textes entre eux. Une mesure couramment utilisée pour les
documents texte est la similarité cosinus, qui calcule la similarité basée sur
les vecteurs de fréquence des mots. Cette mesure est facile à implémenter et
donne généralement de bons résultats.

Prétraitement du texte : Avant de calculer la similarité, vous devez effectuer
un prétraitement du texte pour nettoyer et normaliser les données. Cela peut
inclure la suppression de la ponctuation, des stopwords (mots vides) et d'autres
caractères indésirables. Vous pouvez utiliser des bibliothèques de traitement du
langage naturel (NLP) telles que NLTK (Natural Language Toolkit) pour effectuer
ces étapes.

Vectorisation des documents : Vous devez convertir vos documents textuels en
représentations vectorielles numériques pour les utiliser dans l'algorithme de
clustering. Une approche populaire consiste à utiliser la représentation TF-IDF
(Term Frequency-Inverse Document Frequency) pour attribuer des poids aux mots en
fonction de leur fréquence d'apparition dans un document et leur fréquence
inverse dans l'ensemble du corpus. Une autre approche est d'utiliser des modèles
de plongement de mots tels que Word2Vec ou FastText pour capturer les relations
sémantiques entre les mots.

Algorithme de clustering : Il existe plusieurs algorithmes de clustering que
vous pouvez utiliser, tels que le clustering hiérarchique agglomératif, le
clustering K-means ou le DBSCAN (Density-Based Spatial Clustering of
Applications with Noise). Pour créer un dendrogramme, vous pouvez opter pour le
clustering hiérarchique agglomératif, qui permet de fusionner progressivement
les clusters jusqu'à obtenir une seule partition.

Choix du nombre de clusters : Vous devrez déterminer le nombre optimal de
clusters à former dans votre algorithme. Cela peut être fait en utilisant des
mesures d'évaluation du clustering telles que l'indice de silhouette ou le
coefficient de Dunn. Vous pouvez également essayer plusieurs valeurs de k et
évaluer la cohérence interne et externe des clusters obtenus pour trouver le
meilleur nombre de clusters.

Évaluation des résultats : Une fois que vous avez effectué le clustering, il est
important d'évaluer les résultats pour déterminer si les groupes formés sont
cohérents et significatifs. Vous pouvez examiner les mots les plus fréquents
dans chaque cluster, effectuer une analyse qualitative des textes dans chaque
groupe et utiliser des mesures d'évaluation du clustering pour quantifier la
qualité de la partition obtenue.

### Pretraitement

Suppression des balises XML : Cette étape utilise une expression régulière pour
supprimer toutes les balises XML du texte, en les remplaçant par une chaîne
vide. La complexité de cette étape dépend de la taille du texte et est
généralement linéaire, donc Θ(n), où n est la taille du texte.

Tokenisation : Le texte est divisé en mots ou tokens à l'aide du tokenizer
TweetTokenizer de NLTK. Cette étape a une complexité linéaire, donc Θ(n), où n
est la taille du texte.

Lemmatisation : Chaque mot est lemmatisé à l'aide du stemmer SnowballStemmer de
NLTK. La lemmatisation est le processus de réduction des mots à leur forme de
base ou de lemmes. Cette étape implique une recherche dans un dictionnaire
interne et peut varier en complexité en fonction du nombre de mots à lemmatiser.
Dans le pire des cas, lorsque tous les mots nécessitent une recherche dans le
dictionnaire, la complexité est quadratique, donc Θ(n^2), où n est le nombre de
mots.

Filtrage des mots non pertinents : Les mots non pertinents tels que les
stopwords (mots courants qui n'apportent pas beaucoup de sens) et les mots
spécifiques à supprimer sont filtrés. Cette étape a une complexité linéaire,
donc Θ(n), où n est le nombre de mots après la tokenisation.

En ce qui concerne la complexité globale du prétraitement, elle est généralement
dominée par l'étape de lemmatisation dans le pire des cas, ce qui conduit à une
complexité de Θ(n^2), où n est la taille du texte. Cependant, dans la plupart
des cas, la complexité globale est généralement plus proche de Θ(n) en raison
des optimisations internes des bibliothèques utilisées.

Il est important de noter que la complexité peut varier en fonction des
bibliothèques ou des outils spécifiques utilisés pour chaque étape de
prétraitement. Les estimations de complexité mentionnées ici sont basées sur les
bibliothèques NLTK et les approches utilisées dans le code fourni.

### Vectorisation

La vectorisation est le processus de conversion de données textuelles en
représentations vectorielles numériques, de manière à pouvoir les utiliser dans
des algorithmes de machine learning, tels que le clustering. Dans le cas
spécifique de FastText, qui est un outil d'apprentissage de représentations de
mots, la vectorisation se réfère à la création de vecteurs de mots basés sur
leur contexte et leur signification sémantique.

Voici comment la vectorisation avec FastText fonctionne :

Apprentissage des représentations de mots : Pour commencer, vous devez entraîner
des modèles de représentations de mots à l'aide de FastText. Ces modèles
utilisent des méthodes d'apprentissage automatique pour analyser le contexte et
la signification sémantique des mots dans un grand corpus de texte. En analysant
les co-occurrences de mots, FastText crée des représentations vectorielles qui
capturent les relations entre les mots.

Conversion des mots en vecteurs : Une fois que vous avez entraîné un modèle
FastText, vous pouvez utiliser ce modèle pour convertir des mots en vecteurs.
Chaque mot sera représenté par un vecteur de valeurs numériques. Les dimensions
du vecteur sont déterminées par les paramètres spécifiés lors de l'entraînement
du modèle.

Vecteurs de documents : Pour obtenir des vecteurs de documents, vous pouvez
agréger les vecteurs de mots individuels pour chaque document. Par exemple, vous
pouvez prendre la moyenne des vecteurs de mots, la somme pondérée ou d'autres
méthodes d'agrégation en fonction de votre cas d'utilisation spécifique.

Utilisation des vecteurs dans les algorithmes de clustering : Une fois que vous
avez obtenu les vecteurs de documents, vous pouvez les utiliser comme entrée
pour les algorithmes de clustering tels que le clustering hiérarchique ou
K-means. Ces algorithmes utiliseront les informations contenues dans les
vecteurs pour regrouper les documents similaires.

Il est important de noter que FastText nécessite une étape d'apprentissage
préalable, où vous entraînez un modèle sur un corpus de texte suffisamment large
et représentatif de votre domaine d'intérêt. Cela garantit que les vecteurs
résultants capturent efficacement les informations sémantiques des mots.

De plus, il existe d'autres approches de vectorisation de texte, telles que
TF-IDF, Word2Vec, GloVe, qui peuvent également être utilisées pour convertir des
données textuelles en vecteurs numériques. Le choix de la méthode de
vectorisation dépendra de vos besoins spécifiques et des performances que vous
souhaitez obtenir pour votre tâche de clustering.

#### Vectorisation avec FastText

Dans le cadre de votre recherche avec des textes prétraités où vous avez
appliqué une lemmatisation, voici les étapes à suivre pour la vectorisation :

Choix de la méthode de vectorisation : Comme vous avez déjà prétraité vos textes
en appliquant la lemmatisation, vous pouvez utiliser différentes méthodes de
vectorisation, telles que TF-IDF, Word2Vec, GloVe ou FastText. Chaque méthode a
ses propres avantages et inconvénients, il est donc important de choisir celle
qui convient le mieux à votre tâche et à votre corpus de documents. Dans votre
cas, puisque vous avez déjà téléchargé FastText, vous pouvez l'utiliser pour la
vectorisation.

Entraînement du modèle FastText (optionnel) : Si vous avez un corpus de textes
volumineux et représentatif, vous pouvez envisager d'entraîner votre propre
modèle FastText sur ce corpus. Cependant, si vous ne disposez pas d'un corpus
d'entraînement adéquat, vous pouvez utiliser un modèle FastText pré-entraîné
disponible publiquement, qui a été entraîné sur de grandes quantités de données
textuelles.

Chargement du modèle FastText : Si vous avez choisi d'utiliser un modèle
pré-entraîné, vous devez le charger dans votre code Python. Vous pouvez utiliser
la bibliothèque Gensim pour charger et utiliser des modèles FastText
pré-entraînés.

Conversion des documents en vecteurs : Pour chaque document prétraité, vous
pouvez appliquer la lemmatisation et convertir les mots en vecteurs à l'aide du
modèle FastText chargé. Vous pouvez obtenir le vecteur de chaque mot dans un
document et ensuite agréger ces vecteurs pour obtenir un vecteur de document
global. Vous pouvez choisir de prendre la moyenne des vecteurs de mots ou
d'autres méthodes d'agrégation, en fonction de vos besoins.

### Clustering

#### Definition K-Means

Les k-means sont un algorithme de clustering largement utilisé pour regrouper des données non supervisées en k groupes distincts. L'objectif principal des k-means est de minimiser la variance intra-cluster et de maximiser la variance inter-cluster.

L'algorithme des k-means fonctionne de la manière suivante :

Sélectionnez le nombre de clusters k.
Initialisez aléatoirement k centres de cluster.
Affectez chaque point de données au centre de cluster le plus proche en
utilisant une mesure de distance, généralement la distance euclidienne.
Recalculez les centres de cluster en utilisant la moyenne des points affectés à
chaque cluster.
Répétez les étapes 3 et 4 jusqu'à ce que les centres de cluster convergent ou
que le critère d'arrêt soit atteint (par exemple, un nombre maximum
d'itérations).
L'algorithme des k-means attribue finalement à chaque point de données un label
de cluster correspondant au centre de cluster le plus proche. Les points de
données qui sont assignés au même cluster sont considérés comme similaires les
uns aux autres, tandis que les points de données appartenant à des clusters
différents sont considérés comme différents.

Dans le contexte du code que nous avons utilisé, les k-means sont appliqués sur
les vecteurs de documents obtenus à partir des textes prétraités et lemmatisés.
L'algorithme cherche à regrouper les vecteurs de documents en k clusters
distincts, en utilisant la similarité cosinus comme mesure de distance. Les
labels de cluster attribués à chaque document sont ensuite utilisés pour générer
un dendrogramme qui illustre les relations de similarité entre les documents.
L'algorithme que nous avons développé vise à regrouper les textes de Molière et
de Corneille en utilisant différentes mesures de similarité. L'objectif est
d'identifier les similarités et les différences entre les œuvres des deux
auteurs.

#### Algo

Dans un premier temps, nous avons prétraité les textes en les lemmatisant, ce
qui consiste à réduire les mots à leur forme canonique (leur lemme). Cela permet
de normaliser les mots et de regrouper les formes fléchies ou conjuguées.

Ensuite, nous avons utilisé le modèle FastText pour convertir les documents
textuels en vecteurs numériques. Le modèle FastText est un modèle
d'apprentissage de représentations de mots qui capture les relations sémantiques
entre les mots. Pour chaque document, nous avons agrégé les vecteurs de mots
pour obtenir un vecteur de document représentatif.

Nous avons ensuite appliqué quatre mesures de similarité différentes pour le
clustering : la distance euclidienne, la similarité cosinus et la
similarité de Jaccard.

Pour le K-means, nous avons utilisé l'algorithme de regroupement K-means pour
attribuer chaque document à l'un des cinq clusters prédéfinis. Le K-means est
basé sur la minimisation des distances entre les vecteurs de documents et les
centres de cluster.

- Pour la distance euclidienne, nous avons calculé la distance euclidienne entre
chaque paire de vecteurs de documents. En utilisant cette distance, nous avons
construit un dendrogramme en utilisant l'algorithme de regroupement hiérarchique
complet. Le dendrogramme permet de visualiser les relations de similarité entre
les documents.

- Pour la similarité cosinus, nous avons calculé la similarité cosinus entre
chaque paire de vecteurs de documents. En utilisant cette similarité, nous avons
construit un dendrogramme en utilisant également l'algorithme de regroupement
hiérarchique complet.

- Pour la similarité de Jaccard, nous avons converti les vecteurs de documents en
vecteurs binaires, où chaque valeur indique la présence ou l'absence d'un mot
dans un document. En utilisant ces vecteurs binaires, nous avons calculé la
similarité de Jaccard entre chaque paire de documents. Ensuite, nous avons
construit un dendrogramme en utilisant l'algorithme de regroupement hiérarchique
complet.

La complexité de l'algorithme dépend principalement de deux étapes : la
conversion des documents en vecteurs et la construction des dendrogrammes. La
conversion des documents en vecteurs a une complexité dépendante de la taille du
texte et de la dimensionnalité du modèle FastText utilisé. La construction des
dendrogrammes a une complexité dépendante du nombre de documents. En utilisant
l'algorithme de regroupement hiérarchique complet, la complexité est
généralement de l'ordre de O(n^2 log n), où n est le nombre de documents.

En résumé, notre algorithme utilise la lemmatisation et la vectorisation des
textes pour représenter les documents sous forme de vecteurs numériques.
Ensuite, il applique différentes mesures de similarité pour le clustering et
utilise l'algorithme de regroupement hiérarchique complet pour construire les
dendrogrammes. Cela nous permet d'analyser les similarités et les différences
entre les œuvres de Molière et de Corneille.
