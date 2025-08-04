print("=== Vérificateur d'année bissextile ===\n")
while True:
    try:
        annee = int(input("Veuillez saisir l'année afin de vérifier si elle est bissextile: "))
        condition1 = ((annee % 4) == 0)
        condition2 = ((annee % 400) == 0)
        if condition1 or condition2:
            print(annee,"est une année bissextile.")
            break
        else:
            print(annee,"n'est pas une année bisextile")
            break
    except ValueError:
        print("Erreur!! veuillez entrer une année valide.")