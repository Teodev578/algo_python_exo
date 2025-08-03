while True:
    try:
        sexe = input("Veuillez entrer le sexe de l'habitant (H/F) : ")
        age = int(input("Veuillez entrer l'age de l'habitant : "))
        R1 = sexe == "H" and age >= 20
        R2 = sexe == "F" and age >= 20 and age <= 35
        if R1 or R2:
            print("L'habitant est imposable")
            break
        else:
            print("L'habitant est non imposable")
            break
    except ValueError:
        print("Erreur! Veuillez entrer un  nombre valide...")