while True:
    try:
        largeur = float(input("Veuillez entrer la largeur du rectangle : "))
        longueur = float(input("Veuillez entrer la longueur du rectangle : "))

        # On vérifie si les entrées ne sont pas vides
        if not largeur.strip() or not longueur.strip():
            print("⚠️ Erreur : Les valeurs ne peuvent pas être vides.\n")
            continue

        # On vérifie que les dimensions sont positives
        if largeur <= 0 or longueur <= 0:
            print("⚠️ Erreur : La largeur et la longueur doivent être des nombres positifs.\n")
            continue

        if largeur > longueur:
            print("⚠️ Erreur : La largeur doit être inférieure ou égale à la longueur.\n")
            continue

        perimetre = (longueur + largeur) * 2
        print("✅ Le périmètre du rectangle est de :", perimetre)
        break  # Sort de la boucle après un calcul réussi

    except ValueError as e:
        print(f"Erreur : {e}")
        print("Veuillez entrer un nombre entier (•ᴗ•)\n")
