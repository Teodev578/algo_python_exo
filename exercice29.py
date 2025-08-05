
while True:
    try:
        n = int(input("Veuillez entrer la valeur de n : "))
        s=1
        for i in range(1, n+1):
            s *=i
        print("pour n =",n,", s = ",s)
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (ಠ◡ಠ)\n")