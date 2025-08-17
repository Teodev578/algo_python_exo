while True:
    try:
        print("--- Programme d'échange de valeurs de variables ---")
        A = int(input("Veuillez entrer la valeur de votre nombre entier A : "))
        B = int(input("Veuillez entrer la valeur de votre nombre entier B : "))
        print("Avant l'inversion, A = ",A," , et B = ",B)
        
        #C = A
        #A = B
        #B = C
        A,B = B,A
        print("Après l'inversion, A = ",A," , et B = ",B)
        break

    #on capture l'erreur pour l'attraper, youpi!!
    except Exception as e:
        print(f"Boom!! erreur : {e}")

    #ici si on as une erreur en ce qui concerne les chaines de caractères, ce message s'affiche
    except ValueError:
        print("⚠️ Erreur : Veuillez entrer uniquement des nombres entiers.\n")