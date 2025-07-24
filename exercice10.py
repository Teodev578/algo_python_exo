import math
while True:
    try:
        xa = float(input("Veuillez entrer la valeur du point de xa du point x : "))
        xb = float(input("Veuillez entrer la valeur du point de xb du point x : "))
        ya = float(input("Veuillez entrer la valeur du point de ya du point x : "))
        yb = float(input("Veuillez entrer la valeur du point de yb du point x : "))
        d = (xb-xa)**2+(yb-ya)**2
        ab= math.sqrt(d)
        print("la distance entre A et B est : ",d)
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide...")