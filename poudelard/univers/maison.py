def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prénom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs
    }

    return joueur
