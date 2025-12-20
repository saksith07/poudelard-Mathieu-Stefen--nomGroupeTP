
def initialiser_personnage(nom, prenom, attributs):
    liste_inventaire = []
    liste_sortilege = []
    argent = 100
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": argent,
        "Inventaire": liste_inventaire,
        "Sortilèges": liste_sortilege,
        "Attributs": attributs
    }

    return joueur


def afficher_personnage(joueur):
    print("Profil du personnage :")

    for cle, valeur in joueur.items():


        if cle == "Attributs":
            print("Attributs :")
            for attribut, score in valeur.items():
                print("- {} : {}".format(attribut, score))


        elif cle == "Inventaire" or cle == "Sortilèges":


            if valeur == []:
                contenu = ""
            else:
                liste_propre = []
                for objet in valeur:
                    liste_propre.append(str(objet))
                contenu = ", ".join(liste_propre)


            print("{} : {}".format(cle, contenu))

        # 3. Cas simples
        else:
            print("{} : {}".format(cle, valeur))

def modifier_argent(joueur, montant):
    joueur["Argent"] = joueur["Argent"] + montant


def ajouter_objet(joueur, cle, objet):
    joueur[cle].append(objet)


















