while True:
    try:
        n = int(input("Veuillez saisir le nombre d'équipe : "))
        if n < 0:
            print("⚠️ n doit être un nombre positif")
            continue

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    print("équipe :",i,"à domilice vs équipe :",j)
        
        break
    except ValueError:
        print("Erreur!! veuillez entrer un nombre entier (•ᴗ•)\n")