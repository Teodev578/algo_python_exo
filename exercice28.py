
while True:
    try:
        n = int(input("Veuillez entrer la valeur de n : "))
        s=0
        for i in range(0, n+1):
            s += 10**i
        print("pour n =",n,", s = ",s)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer")