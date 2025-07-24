while True:
    try:
        a = float(input("Veuillez entrer le chiffre 1 : "))
        b = float(input("Veuillez entrer le chiffre 2 : "))
        print("La somme de a + b = ", a+b,"le produit de a et b = ", a*b,"\n la différence b - a  = ", b-a,"la division de b par a = ", b/a)
        break
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide")