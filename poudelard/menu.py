from utils.input_utils import demander_choix
from chapitres import chapitre_1, chapitre_2, chapitre_3, chapitre_4


def afficher_menu_principal():
    print("\n" + "=" * 40)
    print("⚡ BIENVENUE DANS L'AVENTURE POUDLARD ⚡")
    print("=" * 40)


def lancer_choix_menu():

    liste_options = [
        "Lancer l'aventure complète (Chapitres 1 à 4)",
        "Quitter le jeu"
    ]

    continuer = True

    while continuer:
        afficher_menu_principal()

        choix = demander_choix("Que veux-tu faire ?", liste_options)

        if choix == liste_options[0]:

            maisons = {
                "Gryffondor": 0,
                "Serpentard": 0,
                "Poufsouffle": 0,
                "Serdaigle": 0
            }

            print("\n--- 🚂 L'AVENTURE COMMENCE ! ---\n")

            joueur = chapitre_1.lancer_chapitre_1()

            input("\nAppuyez sur Entrée pour lancer le Chapitre 2...")
            joueur = chapitre_2.lancer_chapitre_2(joueur)

            input("\nAppuyez sur Entrée pour lancer le Chapitre 3...")
            joueur = chapitre_3.lancer_chapitre_3(joueur, maisons)

            input("\nAppuyez sur Entrée pour lancer le Chapitre 4 (Quidditch)...")
            chapitre_4.lancer_chapitre4_quidditch(joueur, maisons)


        elif choix == liste_options[1]:
            print("Au revoir, jeune sorcier ! À bientôt.")
            continuer = False