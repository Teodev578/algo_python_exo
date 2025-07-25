while True:
    try:
        n1 = int(input("Veuillez entrer la valeur du chiffre 1 : "))
        n2 = int(input("Veuillez entrer la valeur du chiffre 2 : "))
        if n1*n2>=0:
            n1,n2=n2,n1
            print("Les valeurs des variables ont été échanger car elles sont de même signe.")
            print("Leur nouvelle valeur es n1 =",n1," et n2 =",n2)
            break
        else:
            adition=n1+n2
            produit=n1*n2
            print("les deux chiffres sont de signe contraires.")
            print("n1 + n2 = ",adition," n1 x n2 = ",produit)
            break

    except ValueError:
        print("Veuillez entrer un nombre entier valide...")