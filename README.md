## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

ou via django :
- python3 manage.py test

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

- Transfert de base de donnée => via table intermédiaire ;
  CREATE TABLE new_table_transfert AS SELECT * FROM table_a_copier;

  Une nouvelle table est créé contenant les informations.
  Une fois le transfert effectué, on peut supprimer la table de transfert :
    DROP TABLE new_table_transfert

- Transfert de base de donnée d'une table à une autre ;
  INSERT INTO table1 SELECT * FROM table2;

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Quand un développeur pousser le code sur la branche master :
  - CircleCI lance le processus de compilation => il execute la suite de tests
  - Si les tests passent avec succès, CircleCI lance le processus de conteneurisation avec docker.
  - Si la conteneurisation se passe sans erreur, alors CircleCI lance le processus de deployement.

Pour vérifier les tests manuelement => cf test unitaire

Pour créer une image docker, et lancer l'image docker manuellement
AVEC DOCKER :
  - Dans un terminal, aller à la racine du projet avec la commande cd
  - Ouvrir le DockerFile, commenter la ligne CMD sans bind, et decommenter la ligne CMD avec bind.
    Il faut que l'adresse de gunicorne soit liée à 0.0.0.0 pendant les tests en local.
  - Pour créer l'image docker du projet, lancer la commande : docker build -t [nom_image] .
  [non_image] est le nom que vous donnez à l'image docker créer. Notez le . en fin de commande, qui représente le dossier courant (le dossier du projet qui contient le fichier DockerFile)
  - vérifiez que l'image docker a bien était créée : docker images
  Le nom de votre image doit se trouver dans la liste des images disponibles.
  - Pour lancer le conteneur : docker run --rm [nom_image]
  - Pour stop et supprimer le conteneur : docker ps -a
    - copier l'id du conteneur
    - docker stop [id_conteneur]
    - docker rm [id_conteneur] (si on a pas mis l'option --rm au moment du run)

  - pour supprimer toutes les images dockers et cleaner le systeme une fois que tous les tests sont terminés :
    docker system prune -a

AVEC DOCKER-COMPOSE :
Dans un terminal, à la racine du projet. Le dossier doit contenir un fichier docker-compose.yml
Lancer la commande :
$ docker-compose up
Cette commande va créer une image docker, et lancer le container.

Pour stoper, et supprimer les containers :
$ docker-compose down
