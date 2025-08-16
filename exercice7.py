import math

while True:
    try:
        r = float(input("Veuillez entrer la valeur de votre rayon : "))
        if(r<=0):
            print("Le nombre que vous avez entrer est inférieur ou égale à zero, \nveuillez entrer un nombre positif pour effectuer le calcul...")
            continue
        print("Le volume de votre sphère est de : ", format((4*math.pi*(r**3))/3, ".2f"))
        break

    #on capture l'erreur pour l'attraper, youpi!!
    except Exception as e:
        print(f"Boom!! erreur : {e}")
    
    except ValueError:
        print("Erreur!! Veuillez entrer un nombre valide (•ᴗ•)\n")