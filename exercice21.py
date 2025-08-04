while True:
    try:
        deplacement = int(input("6 à droite, 4 à gauche, 8 en haut et 2 en bas...\nVeuillez entrez le nombre pour vous déplacez: "))
        if deplacement == 6:
            print("Le personnage va à droite.")
            break
        elif deplacement == 4 :
            print("Le personnage va à gauche.")
            break
        elif deplacement == 2:
            print("Le personnage va en haut.")
            break
        elif deplacement == 8:
            print("Le personnage va en haut.")
            break
        else:
            print("Erreur de saisie, le personnage ne bouge pas.")
            continue
    except ValueError:
        print("Erreur de saisie, le personnage ne bouge pas.")