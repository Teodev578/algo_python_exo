import math
while True:
    try:
        a = float(input("Veuillez entrer la valeur de a : "))
        b = float(input("Veuillez entrer la valeur de a : "))
        c = float(input("Veuillez entrer la valeur de a : "))
        delta= (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b+math.sqrt(delta))/(2*a)
            x2 = (-b-math.sqrt(delta))/(2*a)
            print("Delta supérieur à 0 : x1 = ",x1,"et x2 =",x2)
            break
        elif delta == 0: 
            x0 = (-b)/2*a
            print("Delta égal à 0 : x0 = ",x0)
            break
        else:
            print("Pas de solution")
            break
    except ValueError:
        print("Erreur! Veuillez entrer un  nombre valide...")