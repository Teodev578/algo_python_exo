while True:
    try:
        marrakech = 1000000
        agadir = 500000
        annee = 0
        while agadir <= marrakech:
            agadir *= 1.08
            marrakech += 50000
            annee +=1
        print(f"Il faudra {annee} an(s) pour qu'Agadir dépasse Marrakech.")
        break
    except ValueError:
        print("Erreur!! veuillez recommencer (•ᴗ•)\n")