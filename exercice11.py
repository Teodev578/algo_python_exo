while True:
    try:
        r1 = float(input("Veuillez entrer la valeur en ohms de la résistance R1: "))
        r2 = float(input("Veuillez entrer la valeur en ohms de la résistance R2: "))
        r3 = float(input("Veuillez entrer la valeur en ohms de la résistance R3: "))
        rS = r1+r2+r3
        rD = (r1*r2*r3)/(r1*r2+r1*r3+r2*r3)
        
        print("La résistance équivalante en série est de : ",rS," et en dérivation : ", format(rD, ".2f"))
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide...")