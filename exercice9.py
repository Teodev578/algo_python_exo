while True:
    try:
        t = int(input("Veuillez entrer le nombre de seconde que vous souhaitez convertir : "))

        if t < 0:
            print("⚠️ Erreur : Le nombre de secondes ne peut pas être négatif.\n")
            continue

        h = t //3600
        r = t %  3600
        m = r // 60
        s = r % 60

        print(h, "H : ",m, "m : ",s,"s")
        break

    #on capture l'erreur pour l'attraper, youpi!!
    except Exception as e:
        print(f"Boom!! erreur : {e}")

    except ValueError:
        print("Veuillez entrer un nombre entier valide...")