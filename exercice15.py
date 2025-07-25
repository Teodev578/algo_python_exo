while True:
    try:
        age=int(input("Veuillez entrer l'age de l'enfant dont vous coulez connaitre la catégorie d'age : "))
        if age < 6:
            print("L'enfant est trop jeune.")
            break
        elif age >= 6 and age <= 7:
            print("la catégorie de l'enfant est poussin!")
            break
        elif age >= 8 and age <= 9:
            print("la catégorie de l'enfant est pupille!")
            break
        elif age >= 10 and age <= 11:
            print("la catégorie de l'enfant est Minime!")
            break
        elif age >= 12 and age <= 16:
            print("la catégorie de l'enfant est cadet!")
            break
        else:
            print("de n'est plus en enfant! il n'y as pas de catégorie pour cet age.")
        break
    except ValueError:
        print("Erreur! Veuillez entrer un  nombre valide...")