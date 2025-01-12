# Réponses aux questions

# 1. Quelle est la variable ayant le plus d’impact sur les entrées annuelles ?

D’après les analyses réalisées, la variable ayant le plus d’impact sur les entrées annuelles est le nombre de fauteuils. En effet, les entrées moyennes par fauteuil montrent que cette variable est directement liée à la capacité d’accueil des cinémas. Les régions ayant les meilleures performances en termes d’entrées par fauteuil, comme Provence-Alpes-Côte d'Azur et Île-de-France, disposent généralement d’un nombre élevé de fauteuils.

Les visualisations obtenues confirment cette observation, car elles montrent une corrélation forte entre le nombre de fauteuils et les entrées, par rapport aux autres variables.

# 2. Le nombre d’écrans ou de fauteuils est-il un bon prédicteur des entrées ?

Oui, parmi les variables étudiées, le nombre de fauteuils se révèle être un bon prédicteur des entrées. Il reflète directement la capacité d’accueil, qui influence fortement le nombre total de spectateurs qu’un cinéma peut attirer.

En revanche, le nombre d’écrans a un impact plus indirect. Bien qu’il contribue à la diversité des films proposés, il ne garantit pas nécessairement des entrées élevées si la capacité d’accueil est limitée.

Les performances du modèle, mesurées par le R² et le MAE, montrent que le modèle basé sur ces variables permet d’expliquer une grande partie de la variance des entrées annuelles. Cela valide leur pertinence comme prédicteurs, surtout pour le nombre de fauteuils.

# 3. Quels sont les meilleurs et pires résultats en termes d'entrées moyennes par fauteuil ?

# Meilleurs résultats :
# Les trois régions ayant obtenu les meilleures performances en termes d’entrées moyennes par fauteuil sont :

Provence-Alpes-Côte d'Azur
Occitanie
Île-de-France
Pires résultats :

# Les trois régions ayant obtenu les plus faibles performances en termes d’entrées moyennes par fauteuil sont :

Auvergne-Rhône-Alpes
Bretagne
Centre-Val de Loire

Ces résultats ont été calculés à l’aide de la fonction calculate_mean_entries et visualisés avec la fonction plot_top_regions. Ils montrent une disparité intéressante entre les régions, ce qui pourrait être exploré plus en détail dans une analyse future.
