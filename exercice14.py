while True:
    try:
        n=int(input("Veuillez entrer le nombre de photcopie à faire : "))
        if n < 10:
            f=n*10
        elif n < 30:
            f = 10*0.3+(n-10)*0.25
        else:
            f = 10*0.30+(n-10)*0.25+(n-20)*0.20
        print("La facture est de : ",f," dh pour vos ",n,"photocopie...")
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide...")