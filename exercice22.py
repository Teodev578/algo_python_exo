while True:
    try:
        print("**Programme de vérification de nombre paire**\n")
        nombre = int(input("Veuillez entrer votre chiffre à vérifier : "))
        if (nombre % 2) ==1:
            print(nombre,"est un chiffre impaire.")
            break
        else:
            print(nombre,"est un chiffre paire.")
            break
    except ValueError:
        print("Erreur!! veuillez entrer un nombre valide. (ex: 1; 2; 9...)")