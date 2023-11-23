# Use Case Beev 

Dans ce git, nous avons : 
- 2 csv contenant les données de voitures
- un fichier .yml contenant les informations afin d'initialiser la BDD
- un fichier main.py qui contient le script permettant d'insérer les données dans la BDD mais aussi d'afficher un graphique montrant l'évolution de ventes de véhicules electriques et thermiques par année
- un fichier query.sql  qui contient les query sql demandées

Voici les différentes étapes afin de réaliser ce use case :

1. Stockez tous les documents dans un repository 
2. Installez docker
3. Executez un terminal à partir de ce dossier et lancez la commande : docker-compose up -d
5. Maintenant, installez par exemple pgAdmin, créez un serveur et ajoutez les informations présentes dans le .yml
La connexion est maintenant réalisé entre le docker et pgAdmin
6. Installez les librairies pandas, sqlalchemy et matplotlib.pyplot
7. Lancez votre IDE et executez le script python
Les données sont chargés dans la BDD virtuel, de plus la query vous retourne un graphique
8. Dans le fichier query.sql se trouvent les query à utiliser dans pgAdmin afin de faire des requêtes
