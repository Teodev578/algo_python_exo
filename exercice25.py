print("=== 10 nombres suivants ===\n")
while True:
    try:
        n = int(input("Veuillez entrer votre chiffre."))
        for i in range(n+1, n+11):
            print(i, end=" ")
        break
    except ValueError:
        print("Erreur!! veuillez recommencer")