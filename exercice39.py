while True:
    print("---- Calculatrice menu ----")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Reste d'une division")
    print("6. Puissance")
    print("0. Quitter\n")

    try:
        operation = int(input("Choisissez une option (1-6) ou 0 pour quitter: "))
        if operation == 1:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print(f"Résultat: {a + b}")

        elif operation == 2:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print(f"Résultat: {a - b}")

        elif operation == 3:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            print(f"Résultat: {a * b}")

        elif operation == 4:
            a = float(input("Entrez le premier nombre: "))
            b = float(input("Entrez le deuxième nombre: "))
            if b == 0:
                print("Erreur: Division par zéro.")
            else:
                print(f"Résultat: {a / b}")

        elif operation == 5:
            a = int(input("Entrez le premier nombre: "))
            b = int(input("Entrez le deuxième nombre: "))
            if b == 0:
                print("Erreur: Division par zéro.")
            else:
                print(f"Résultat: {a % b}")

        elif operation == 6:
            a = float(input("Entrez la base: "))
            b = float(input("Entrez l'exposant: "))
            print(f"Résultat: {a ** b}")
        elif operation == 0:
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

    except ValueError:
        print("Oops... On dirait que vous n'avez pas entrer un nombre valide.\n")