while True:
    try:
        largeur = float(input("Veuillez entrer la largeur du rectangle : "))
        longueur = float(input("Veuillez entrer la longueur du rectangle : "))

        if largeur > longueur:
            print("⚠️ Erreur : La largeur doit être inférieure ou égale à la longueur.\n")
            continue  # Recommence la boucle

        perimetre = (longueur + largeur) * 2
        print("✅ Le périmètre du rectangle est de :", perimetre)
        break  # Sort de la boucle après un calcul réussi

    except ValueError:
        print("⚠️ Erreur : veuillez entrer des nombres valides.\n")
