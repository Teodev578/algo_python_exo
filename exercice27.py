
while True:
    try:
        n = int(input("Veuillez entrer la valeur de n : "))
        s=0
        for i in range(1, n+1):
            s += 1/i
        print("pour n =",n,", s = ",format(s, ".2f"))
        break
    except ValueError:
        print("Erreur!! veuillez recommencer")