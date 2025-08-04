print("=== Vérificateur de caractères ===\n")
while True:
    try:
        caractere = input("Veuillez saisir quelque chose: ")
        if ("A" < caractere and "Z" > caractere) or ("a" < caractere and "z" > caractere):
            print("Le caractère",caractere," est un alphabet")
            break
        elif ("0" < caractere and "9" > caractere):
            print("Le caractère",caractere," est un nombre")
            break
        else:
            print("Le caractère",caractere," est un caractère spéciale")
            break
    except ValueError:
        print("Erreur!! veuillez recommencer")