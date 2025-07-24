while True:
    try:
        print("Programme échange de valeur de variable:")
        A = int(input("Veuillez entrer la valeur de votre nombre entier A : "))
        B = int(input("Veuillez entrer la valeur de votre nombre entier B : "))
        print("Avant l'inversion, A = ",A," , et B = ",B)
        
        #C = A
        #A = B
        #B = C
        A,B = B,A
        print("Après l'inversion, A = ",A," , et B = ",B)
        break
    except ValueError:
        print("Veuillez entrer un nombre valide...")