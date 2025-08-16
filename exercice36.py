while True:
    try:
        n = int(input("Veuillez saisir votre nombre : "))
        estPremier = 1
        for i in range(2, int(n/2)):
            if (n%i==0):
                estPremier=0
                break
        
        if estPremier ==1:
            print(n,"est nombre premier")
        else:
            print(n,"est un nombre non premier")
        break
    except ValueError:
        print("Erreur!! veuillez entrer un nombre entier (•ᴗ•)\n")