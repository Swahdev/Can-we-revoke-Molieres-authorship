# Traduction

Pour mesurer les similarités entre des textes, différents ensembles de
caractéristiques peuvent être quantifiés, qu'il s'agisse de caractéristiques
lexicales (lemmes, lemmes en rimes, formes de mots) ou grammaticales (affixes,
parties du discours, mots fonctionnels). Pour chacun de ces six types de
caractéristiques, les textes sont triés selon un algorithme de classification
hiérarchique, suivant une procédure testée avec succès sur un corpus de comédies
en vers de l'époque postérieure à la mort de Molière et de Corneille (voir
Matériel et Méthodes). Nous effectuons d'abord une analyse exploratoire sur un
grand corpus de pièces de théâtre de l'époque de Molière. Nous analysons ensuite
un corpus de pièces appartenant au même sous-genre que les grandes comédies
signées par Molière.

Caractéristiques étudiées
Lexique
En la matière, les études fondatrices de C. et D. Labbé se sont concentrées sur
les fréquences des lemmes ou formes canoniques des mots (c'est-à-dire que
"aimer" est le lemme de "aimant", "aimé", "(il) aime", etc.). Ces
caractéristiques dépendent fortement du sujet ou du genre littéraire d'un texte.
Les étudier est néanmoins utile dans notre contexte : si notre hypothèse H1
était vraie, alors les pièces de théâtre de P. Corneille et de Molière devraient
différer selon ce critère, mais montrer des similarités selon tous les autres
angles.

Lexique de rimes
Les mots choisis pour la rime sont soigneusement sélectionnés par l'auteur et
sont parfois considérés comme spécifiques à un auteur (24). Bien sûr, les mots
utilisés pour la rime dépendent toujours du sujet de la pièce, et les
similarités dans le vocabulaire de rimes peuvent facilement résulter d'une
imitation intentionnelle ou d'une inspiration inconsciente. De plus,
l'échantillon des lemmes utilisés en position de rime est un sous-ensemble
sensiblement plus petit de l'échantillon contenant tous les lemmes d'un texte.

Formes de mots
Les formes brutes (c'est-à-dire non lemmatisées) des mots sont parfois
considérées comme révélatrices du style de l'auteur : bien qu'elles dépendent
encore largement du contenu des textes, l'absence de lemmatisation permet la
préservation de certaines informations morphologiques (l'inflection des noms et
des verbes), ce qui peut être utile dans une langue flexionnelle comme le
français.

Affixes
Les n-grammes de caractères de n-contiguës - c'est-à-dire, des séquences de n
caractères contigus - sont souvent considérés comme une caractéristique très
efficace pour l'attribution de l'auteur (25). Leur efficacité semble venir de
leur capacité à capturer les morphèmes grammaticaux, en particulier les préfixes
et les suffixes, ainsi que la ponctuation de l'auteur lorsqu'elle est disponible
(26). En l'absence de ponctuation de l'auteur, nous limitons notre analyse des
n-grammes de caractères à quatre types d'affixes: les trois premiers ou derniers
caractères des mots d'au moins quatre caractères, ainsi que l'espace inter-mots
avec les deux caractères précédents ou suivants (26).

Séquences morphosyntaxiques
Les différences en morphosyntaxe sont considérées comme un indice important pour
déterminer l'auteur d'un texte. Une approche possible est d'analyser les
séquences de classes de mots ou de parties du discours (POS). Les n-grammes POS,
en particulier les 3-grammes POS (c'est-à-dire, les séquences d'étiquettes,
telles que "NOM ADJECTIF VERBE"), se sont révélés être des critères efficaces
pour découvrir l'auteur d'un texte, surpassés seulement par les mots
fonctionnels (27).

Mots fonctionnels
Selon la littérature des 3 dernières décennies, l'analyse des mots fonctionnels
est la méthode la plus fiable pour l'attribution de l'auteur littéraire (25,
28). L'intuition sous-jacente est que les mots fonctionnels sont utilisés
principalement selon des modèles inconscients et varient moins en fonction des
sujets ou du genre des textes. Des études de psycholinguistique ont montré que
les mots fonctionnels sont perçus par les lecteurs à un niveau moins conscient
et sont lus plus rapidement que les mots de contenu ; ils pourraient également
être choisis moins consciemment par les auteurs, tout en étant capables de
transmettre des informations significatives sur le locuteur ou l'écrivain (25,
29). Partagés par tous les écrivains, les mots fonctionnels sont également
intéressants d'un point de vue statistique, car le nombre de mots fonctionnels
distincts dans une langue est faible (par exemple, environ 100 en français),
mais leur nombre d'occurrences dans un texte est très élevé (25, 29).

Analyse exploratoire
Nous effectuons d'abord une analyse exploratoire d'un grand échantillon de
comédies en vers, en utilisant les éditions numériques de Fièvre (30). Cet
échantillon comprend des pièces d'au moins 5000 mots, pour des auteurs ayant
écrit au moins trois comédies. Il comprend des pièces de 12 auteurs. Les
résultats sont affichés dans la figure 1.
