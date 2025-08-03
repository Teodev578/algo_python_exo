while True:
    try:
        a = float(input("Veuillez saisir la valeur de A : "))
        op = input("Veuillez saisir l'opérateur : ")
        b = float(input("Veuillez saisir l'opérateur : "))
        if op == "+":
            print("A + B = ",a+b)
            break
        elif op == "-":
            print("A - B = ",a-b)
            break
        elif op == "/":
            if a == 0:
                print("Pas de solution pour cette division, tout nombre sur zero est égale à infini : ")
            else:
                print("A / B = ",a/b)
            break
        elif op == "*":
            print("A * B = ",a*b)
            break
        else:
            print("Opérateur invalide.")
            continue
    except ValueError:
        print("Erreur! Veuillez entrer une valeur valide...")