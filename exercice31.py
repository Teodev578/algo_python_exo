while True:
    try:
        n = int(input("Veuillez entrer la valeur de n : "))
        if n <= 0:
            n = int(input("Veuillez entrer la valeur de n : "))
            continue
        print("Les diviseurs de ",n,"sont : ")
        for i in range(1, n+1):
            if (n % i == 0):
                print(i)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (•ᴗ•)\n")