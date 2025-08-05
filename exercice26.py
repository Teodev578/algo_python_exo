print("=== 10 nombres suivants ===\n")
while True:
    try:
        n = int(input("Veuillez entrer votre chiffre."))
        i=n+1
        while i <= n+10:
            print(i, end=" ")
            i+=1
        break
    except ValueError:
        print("Erreur!! veuillez recommencer")