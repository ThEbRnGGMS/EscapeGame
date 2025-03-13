import random
import time

def ASCII_Entree():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE     ENTREE     DROITE│    │
│    │◄─────                ─────►│    │
│    │             ┌─────────┐    │    │
│    │             │         │    │    │
│    │             │  PORTE  │    │    │
│    │             |         │    │    │
│    │   COMMODE   │         │    │    │
│    │ ┌────┬────┐ │○──      │    │    │
│    │ │    │    │ │         │    │    │
│    │ │   •│•   │ │         │    │    │
│    │ │    │    │ │         │    │    │
│    └─│    │    │─┴─────────┴────┘    │
│   /  └─┬──┴──┬─┘                 \   │
│  /     │     │                    \  │
│ /                                  \ │
│/                                    \│
└──────────────────────────────────────┘
""")

def ASCII_Cuisine():
    print("""
┌────┬────────────────────────────┬────┐
│    │          CUISINE     DROITE│    │
│    │                      ─────►│    │
│    │   ┌────┬────┐┌────┬────┐   │    │
│    │   │   •│•   ││   •│•   │   │    │
│    │   │    │    ││    │    │   │    │
│    │   └────┴────┘└────┴────┘   │    │
│    └────────────────────────────┘    │
│   /                              \   │
│  /                                \  │
│ ┌─────────┬─────────┬──────────────┐ │
│ │ PLACARD │         │ ┌──────────┐ │ │
│ │        │││        │ │ ──────── │ │ │
│ │        │││        │ │   FOUR   │ │ │
│ │         │         │ │          │ │ │
│ └─────────┴─────────┴─└──────────┘─┘ │
│/                                    \│
└──────────────────────────────────────┘
""")

def ASCII_Salon():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE      SALON     DROITE│    │
│    │◄─────                ─────►│    │
│    │                            │    │
│    │                            │    │
│    │             \/             │    │
│    │         ┌────────┐         │    │
│    │         │   TV   │         │    │
│    │         │        │         │    │
│    │         └─┬────┬─┘         │    │
│    │     ┌─────┴────┴─────┐     │    │
│    │     │                │     │    │
│    └─────│                │─────┘    │
│   /      └─┬────────────┬─┘      \   │
│  /  ┌──────────────────────────┐  \  │
│ /   │          TAPIS           │   \ │
│/    └──────────────────────────┘    \│
└──────────────────────────────────────┘
""")

def ASCII_Salle_Jeux():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE   Salle Jeux   DROITE│    │
│    │◄─────                ─────►│    │
│    │                            │    │
│    │      ┌──────────────┐      │    │
│    │      │   TOY BOX    │      │    │
│    │      │   (⊙▂⊙)      │      │    │
│    │      └──────────────┘      │    │  
│    │      ┌──────────────┐      │    │
│    │      │   ÉTAGÈRE    │      │    │
│    │      │ (⚽ 🧸 🎲)   │      │    │
│    │      └──────────────┘      │    │
│    └────────────────────────────┘    │
│   /                              \   │
│  /                                \  │
│ /                                  \ │
│/                                    \│
└──────────────────────────────────────┘
""")

def ASCII_Chambre_fermee():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE     CHAMBRE    DROITE│    │
│    │◄─────                ─────►│    │
│    │  ┌─────────┐               │    │
│    │  │         │               │    │
│    │  │  PORTE  │               │    │
│    │  │         │               │    │
│    │  │         │               │    │
│    │  │○──      │               │    │
│    │  │         │               │    │
│    │  │         │               │    │
│    │ ZZZZ       │               │    │
│    └──┴──zz─────┴───────────────┘    │
│   /        |\      _,,,---,,_    \   │
│  /         /,`.-'`'    -.  ;-;;,_ \  │
│ /         |,4-  ) )-,_. ,\ (  `'-' \ │
│/         '---''(_/--'  `-'\_)       \│
└──────────────────────────────────────┘
""")

def ASCII_Chambre_ouverte():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE    CHAMBRE     DROITE│    │
│    │◄─────                ─────►│    │
│    │                ┌─────────┐ │    │
│    │                │         │ │    │
│    │                │ TABLEAU │ │    │
│    │   _            │         │ │    │
│    │  / \           │         │ │    │
│    │ /   \ ┌───────┐│         │ │    │
│    │ └─┬─┘ │┌─┐ ┌─┐│└─────────┘ │    │
│    │   │   │└─┘ └─┘│            │    │
│    │┌──┴──┐├───────┤            │    │
│    └│LAMPE││       │────────────┘    │
│   / └─────┘│       │             \   │
│  /         │       │              \  │
│ /          ├───────┤               \ │
│/           │       │                \│
└──────────────────────────────────────┘
""")

def Entree():
    ASCII_Entree()
    global code_cadenas
    while True:

        # Demander au joueur ce qu'il veut faire
        action = input("Vous êtes dans l'entrée. Que voulez-vous faire ? (COMMODE, PORTE, GAUCHE, DROITE) ").upper()

        # Interagir avec les objets
        if action == "COMMODE":
            print(">>>>> Le chiffre _ _ _ " + code_cadenas[3] + " a été gravé sur le dessus de la commode")

        elif action == "PORTE":
            tentative = input(">>>>> Entrez le code à 4 chiffres : ")
            if tentative == code_cadenas:
                print(">>>>> Bravo ! Vous vous êtes échappés !")
                exit()
            else:
                print(">>>>> Mauvais code.")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Salle_de_jeux()

        elif action == "DROITE":
            Chambre()

        else:
            print(">>>>> Action invalide.")

def Cuisine():
    ASCII_Cuisine()
    global possede_pile_B
    while True:

        # Demander au joueur ce qu'il veut faire
        action = input("Vous êtes dans le salon. Que voulez-vous faire ? (PLACARD, FOUR, DROITE) : ").upper()

        # Interagir avec les objets
        if action == "PLACARD":
            possede_pile_B = True
            print(">>>>> Vous trouvez une pile !")

        elif action == "FOUR":
            print(">>>>> Vous venez de découvrir un nouveau code !!!! Le code : " + code_cadenas[0] + " _ _ _ a était écris sur une feuille")

        # Se déplacer dans le jeu
        elif action == "DROITE":
            Salle_de_jeux()


        else:
         print(">>>>> Action invalide.")

def Salon():
    ASCII_Salon()
    global possede_cle_chambre
    while True:

        # Demander au joueur ce qu'il veut faire
        action = input("Vous êtes dans le salon. Que voulez-vous faire ? (TAPIS, TV, GAUCHE, DROITE) ").upper()

        # Interagir avec les objets
        if action == "TAPIS":
            print(">>>>> Vous trouvez une clé.")
            possede_cle_chambre = True

        elif action == "TV":
            if possede_pile_A and possede_pile_B:
                print(">>>>> La télévision s'allume, et on peut lire _ " + code_cadenas[1] + " _ _ sur l'écran")
            else:
                print(">>>>> La TV a besoin de 2 piles pour s'allumer")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Chambre()

        elif action == "DROITE":
            Salle_de_jeux()

        else:
            print(">>>>> Action invalide.")

def Chambre():
    ASCII_Chambre_fermee()
    global possede_pile_A
    while True:

        # Demander au joueur ce qu'il veut faire
        action = input("Vous êtes devant la chambre. Que voulez-vous faire ? (PORTE, GAUCHE, DROITE) ").upper()

        # Interagir avec les objets
        if action == "PORTE":
            if possede_cle_chambre:
                ASCII_Chambre_ouverte()
                while True:
                    action2 = input("Vous ouvrez la chambre avec la clef. Que voulez-vous faire ? (LAMPE, TABLEAU, GAUCHE, DROITE) ").upper()
                    if action2 == "LAMPE":
                        possede_pile_A = True
                        print(">>>>> Vous trouvez une pile !")
                    elif action2 == "TABLEAU":
                        print(">>>>> Vous décrochez le tableau, et voyez qu'un _ _ " + code_cadenas[2] + " _ a été peint sur le mur")
                    elif action2 == "GAUCHE":
                        Entree()
                    elif action2 == "DROITE":
                        Salon()
                    else:
                        print(">>>>> Action invalide.")
            else :
                print(">>>>> La chambre est fermée à clef... ")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Entree()

        elif action == "DROITE":
            Salon()

        else:
            print(">>>>> Action invalide.")

def Salle_de_jeux():
    ASCII_Salle_Jeux()
    global possede_dé
    while True:

        # Demander au joueur ce qu'il veut faire
        action = input("Vous êtes dans la salle de jeu. Que voulez-vous faire ? (ETAGERE, TOYBOX, GAUCHE, DROITE) : ").upper()

        # Interagir avec les objets
        if action == "ETAGERE":
            possede_dé = True
            print(">>>>> Vous trouvez un dé !")

        elif action == "TOYBOX":
            print(">>>>> Vous venez de découvrir un nouveau son de kerchak")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Cuisine()
        elif action == "DROITE":
            Entree()


        else:
         print(">>>>> Action invalide.")

# Initialisation du jeu
code_cadenas = str(random.randint(1111, 9999))
possede_pile_B = False
possede_pile_A = False
possede_cle_chambre = False
possede_dé = False

# Commence le jeu dans la fonction "Entree"
Entree()
