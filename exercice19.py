while True:
    try:
        prix = float(input("Veuillez entrer le prix du produit : "))
        cat = input("Veuillez entrer la catégorir du produit (A/B/C) : ")
        if cat == "A":
            tva = prix*0.07
            print("Le client va payer : " ,prix-tva)
            break
        elif cat =="B":
            tva = prix*0.20
            print("Le client va payer : " ,prix-tva)
            break
        elif cat =="C":
            tva = prix*0.25
            print("Le client va payer : " ,prix-tva)
            break
        else:
            print("Cette catégorie est invalide ")
            continue
    except ValueError:
        print("Erreur! Veuillez entrer une valeur valide...")