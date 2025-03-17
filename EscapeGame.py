import random
import time

def decompteDe():
    global code_cadenas
    dè = [1, 2, 3, 4, 5, 6]  # Liste des valeurs du dé
    tour_des = 0

    ASCII_Salle_Jeux()

    print(">>>>> Vous jetez les dès !!!!")

    while tour_des < 7:

        choix_des = random.choice(dè)  # Sélection aléatoire d’un nombre

        time.sleep(1)

        print(f"Lancer du dé : {choix_des}   ", end='\r', flush=True)  # Effet de roulage du dé
        time.sleep(0.5)  # Pause de 0.5 seconde entre chaque affichage
        tour_des += 1

    print(f"\nRésultat final : {choix_des}")  # Affichage final propre

    if choix_des == 6:
        print(">>>>> Le chiffre _ _ _ _ " + code_cadenas[4] + " a été gravé sur le dessus de la commode")

        time.sleep(3)

        ASCII_Salle_Jeux_Fini()
    
    elif choix_des != 6:
        print(">>>>> Veuillez encore tourner le dès jusqu'à avoir le chiffre 6.")

        time.sleep(3)

        ASCII_Salle_Jeux()

    time.sleep(1)

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
│    │GAUCHE    CUISINE     DROITE│    │
│    │◄─────                ─────►│    │
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

def ASCII_Salle_Jeux_Fini():
    print("""
┌────┬────────────────────────────┬────┐
│    │GAUCHE   Salle Jeux   DROITE│    │
│    │◄─────                ─────►│    │
│    │                            │    │
│    │                            │    │
│    │                            │    │
│    │      ┌──────────────┐      |    |
|    |      │   ÉTAGÈRE    │      |    |
|    |      │ (⚽ 🧸 🎲)   │      |    |
|    |      └──────────────┘      │    │
│    │                            │    │  
│    │                            │    │
│    │                            │    │
│    │                            │    │
│    │                            │    │
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
            print(">>>>> Le chiffre _ _ " + code_cadenas[2] + " _ _ a été gravé sur le dessus de la commode")

        elif action == "PORTE":
            tentative = input(">>>>> Entrez le code à 5 chiffres : ")
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
            print(">>>>> Vous venez de découvrir un nouveau code !!!! Le code :  _ _ _ " + code_cadenas[3] + " _ a était écris sur une feuille")

        # Se déplacer dans le jeu
        elif action == "DROITE":
            Salle_de_jeux()

        elif action == "GAUCHE":
            Cuisine()

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
                print(">>>>> La télévision s'allume, et on peut lire " + code_cadenas[0] + " _ _ _ _ sur l'écran")
            else:
                print(">>>>> La TV a besoin de 2 piles pour s'allumer")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Chambre()

        elif action == "DROITE":
            Salon()

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
                        print(">>>>> Vous décrochez le tableau, et voyez qu'un _ " + code_cadenas[1] + " _ _ _ a été peint sur le mur")
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
            ASCII_Salle_Jeux()
            possede_dé = True
            print(">>>>> Vous trouvez un dé !")

        elif action == "TOYBOX":
            
            if possede_dé == True:
                decompteDe()

            if possede_dé == False:
                print(">>>>> Vous avez besoin d'un dè pour continuer")

        # Se déplacer dans le jeu
        elif action == "GAUCHE":
            Cuisine()
        elif action == "DROITE":
            Entree()


        else:
         print(">>>>> Action invalide.")

# Initialisation du jeu
code_cadenas = str(random.randint(11111, 99999))
possede_pile_B = False
possede_pile_A = False
possede_cle_chambre = False
possede_dé = False

# Commence le jeu dans la fonction "Entree"
Entree()
