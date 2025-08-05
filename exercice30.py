
while True:
    try:
        n = int(input("Veuillez entrer la valeur de n : "))
        s=0
        j=1
        for i in range(1, n+1):
            s += j**2
            j=j+2
        print("pour n =",n,", s = ",s)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (•ᴗ•)\n")