# P4_konrath_kevin

P4 Développez un programme logiciel en Python

____
## Lancer le logiciel Mac / Linux :


### 1. Récupérr le projet :

`$ git clone https://github.com/Ikeaven/P4_konrath_kevin.git`


Dans un terminal, aller dans le dossier de l'application.

`$ cd P4_konrath_kevin`
### 2. Créer et activer un environnement virtuel :

`$ python3 -m venv env`

`$ source env/bin/activate`

### 3. Installer les dépendances :

`pip install -r requirements.txt`

### 4. Lancer l'application

`python main.py`


____
## initialisation du projet Windows:

Dans Windows PowerShell : Naviguez vers le repertoire souhaité, à l'aide de cd / ls

### 1. Récupérer le projet

`$ git clone https://github.com/Ikeaven/P4_konrath_kevin.git`

### 2. activer un environnement vituel

`$ cd P4_konrath_kevin`

`$ py -m venv env`

`$ .\env\Scripts\activate`

### 3. installer les dépencances projets

`$ pip install -r requirements.txt`

### 4. executer le programme :

`$ py main.py`

## Générer rapport html Flake8-html

Dans le terminal ou PowerShell, à la racine du projet :

`$ flake8 --format=html --htmldir=flake8_report`
<br/>
# Utilisation

Naviguer d'un menu à l'autre avec les numéros de menu.
## Menu principal:
1. Créer un nouveau tournoi
2. Ajouter un nouveau joueur
3. Editer un tournoi
4. Editer un joueur
5. Rapports
6. Chargement de la base de donnée
7. Sauvegarder
8. DEMO : générer un tournoi automatiquement
9. Quitter

### [1] Créer un nouveau tournoi
Une série de champs d'entrées vont apparâtre dans la console. <br/>
Remplissez les champs pour créer un tournoi

### [2] Ajouter un nouveau joueur
Une série de champs d'entrée vont apparaître dans la console. <br/>
Remplissez les champs pour créer un joueur.
### [3] Menu Edition tournoi:
La liste des tournois va vous être présenté si vous avez déjà renseigné des tournois ou importé depuis la base de données.
Selectionner le tournoi grace à l'index associé.

Vous pouvez maintenant modifier le tournoi selectionné grace au menu d'édition:
1. Fin de round et mise à jour de socre
2. Changer le nom
3. Changer la description
4. Changer le controller de temps
5. Changer la localisation
6. Changer la date de début du tournoi
7. Changer la date de fin du tournoi
8. Retour au menu principal

### [4] Menu edition d'un joueur:
La liste des joueurs va vous être présenté si vous avez déjà rensigné des joueurs ou importé des joueurs de la base de données.
Selectionner le joueur grace à l'index associé.

Vous pouvez maintenant modifier les informations du joueur grace au menu d'édition:
1. Editier le classement
2. Editier Nom et prénom
3. Editer la date d'anniversaire
4. Editer le sexe
5. Retour au menu principal

### [5] Menu des Rapports
1. Liste des acteurs (tous les joueurs)
2. Liste des joueurs d'un torunoi
3. Liste des tournois
4. Liste des tours d'un tournoi
5. Liste des matchs d'un tournoi
6. Score finale : pour les tournois terminés
7. Retour au menu principal

### [6] Chargement de la base de données:

Récupération des informations déjà sauvegardées.

### [7] Sauvegarder
Sauvegarder les éléments dans la base de données.

### [8] DEMO: générer un tournoi automatiquement:
ATTENTION: pour tester l'application uniquement !! <br/>
Génère un tournoi automatiquement pour tester l'application sans avoir a saisir des informations manuellement.

### [9] Quitter l'application
Sortir de la boucle de l'application
