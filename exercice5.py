while True:
    try:
        a = float(input("Veuillez entrer le premier nombre (non-nul) : "))
        b = float(input("Veuillez entrer le deuxième nombre : "))

        # Validation de l'entrée a pour éviter la division par zéro
        if a == 0:
            print("⚠️ Erreur : Le premier nombre ne peut pas être zéro car la division par zéro est indéfinie.\n")
            continue  # Revient au début de la boucle

        # Calculs
        somme = a + b
        produit = a * b
        difference = b - a
        division = b / a

        # Affichage des résultats
        print(f"✅ La somme de {a} et {b} est : {somme}")
        print(f"✅ Le produit de {a} et {b} est : {produit}")
        print(f"✅ La différence de {b} et {a} est : {difference}")
        print(f"✅ La division de {b} par {a} est : {division}")
        break

    except ValueError as e:
        print(f"Erreur : {e}")
        print("⚠️ Erreur : Veuillez entrer des nombres valides.\n")