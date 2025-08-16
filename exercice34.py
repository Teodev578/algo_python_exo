while True:
    try:
        n = int(input("veuillez entrer la valeur de n : "))
        if n <= 0:
            n = int(input("veuillez entrer la valeur de n : "))
            continue
        u = 6
        #print("Les diviseurs de ",n,"sont : ")
        #1,2,...,n+1
        for i in range(1, n+1):
            u = 4*u+10
        print("U",n," = ",u)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (•ᴗ•)\n")