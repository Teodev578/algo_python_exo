while True:
    try:
        n = int(input("Veuillez entrer le rang n : "))
        if n < 2:
            print("⚠️ n doit être supérieur ou égal à 2.")
            continue

        upp = 0
        up = 1

        print("Les termes de la suite de Fibonacci sont : ")
        print(upp, end=" ")
        print(up, end=" ")

        for _ in range(n - 2):  # déjà 2 termes affichés
            U = upp + up
            print(U, end=" ")
            upp = up
            up = U

        print()  # saut de ligne final
        break

    except ValueError:
        print("Erreur!! veuillez entrer un nombre entier (•ᴗ•)\n")
