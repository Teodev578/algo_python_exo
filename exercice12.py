while True:
    try:
        n1 = int(input("Veuillez entrer la valeur du chiffre 1 : "))
        n2 = int(input("Veuillez entrer la valeur du chiffre 2 : "))
        if(n1*n2<0):
            print("Vos deux chiffres sont de signe contraires : ")
            break
        else:
            print("Vos deux chiffres sont de même signe : ")
            break

    except ValueError:
        print("Veuillez entrer un nombre entier valide...")