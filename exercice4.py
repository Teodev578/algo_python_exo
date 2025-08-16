while True:
    try:
        largeur = float(input("Veuillez entrer la largeur du rectangle : "))
        longueur = float(input("Veuillez entrer la longueur du rectangle : "))

        # Vérification des dimensions positives
        if largeur <= 0 or longueur <= 0:
            print("⚠️ Erreur : La largeur et la longueur doivent être des nombres positifs et non nuls.\n")
            continue

        if largeur > longueur:
            print(" ⚠️ Erreur : La largeur de notre rectangle doit être inférieure ou égale à la longueur.\n")
            continue  # Recommence la boucle

        perimetre = (longueur + largeur) * 2
        surface = longueur * largeur
        print(" ✅ Le périmètre de votre rectangle est de :", perimetre, " et sa surface : ", surface)
        break  # Sort de la boucle après un calcul réussi

    except ValueError as e:
        print(f"Erreur : {e}")
        print("Veuillez entrer un nombre entier (•ᴗ•)\n")
