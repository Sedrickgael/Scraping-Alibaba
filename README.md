# Scraping Alibaba.com - Product Information Scraper

## Description

Ce projet est un **scraper de produits** pour le site [Alibaba.com](https://www.alibaba.com), utilisant les bibliothèques Python `requests` et `Selenium`. Il permet d'extraire des informations sur les produits (images, descriptions, prix, etc.) à partir de différentes catégories disponibles sur le site.

Les données collectées sont ensuite stockées dans des fichiers JSON ou CSV pour une analyse ultérieure, et peuvent être affichées sur une page web générée automatiquement.

## Fonctionnalités

- **Scraping automatisé** des catégories et sous-catégories de produits
- **Extraction d'informations détaillées** sur chaque produit (titre, prix, image, description, etc.)
- **Téléchargement d'images** de produits
- Sauvegarde des données collectées au format **JSON** ou **CSV**
- **Affichage des données** sur une page web (`index.html`)
- Organisation des produits par **catégorie** et **sous-catégorie**
- Utilisation de **Selenium** pour interagir avec la barre de navigation et survoler les sous-catégories

## Pré-requis

Avant de pouvoir exécuter ce projet, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- Connaissances de base en **CSS** et **JavaScript**
- Google Chrome ou un autre navigateur compatible
- [Google ChromeDriver](https://sites.google.com/chromium.org/driver/) (assurez-vous d'avoir la bonne version pour votre navigateur)
- Les bibliothèques Python suivantes :
  - `selenium`
  - `requests`
  - `json`

## Installation

1. Clonez ce projet sur votre machine locale :
   ```bash
   git clone https://github.com/votre-nom-utilisateur/scraping-alibaba.git
2. Installez les dépendances Python 
    selenium==4.1.0
    requests==2.26.0
    ```bash
    pip install -r requirements.txt
 
