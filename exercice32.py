while True:
    try:
        n = int(input("Quel anniversaire fêteras Amal cette année? : "))
        if n <= 0:
            n = int(input("Veuillez entrer la valeur de n : "))
            continue
        s = 0
        #print("Les diviseurs de ",n,"sont : ")
        for i in range(1, n+1):
            s += 500 +  i*3
        print("Pour son",n,"ième anniversaire la somme sur son compte sera de : ",s)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (•ᴗ•)\n")