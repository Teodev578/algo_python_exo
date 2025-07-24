while True:
    try:
        t = int(input("Veuillez entrer le nombre de seconde que vous souhaitez convertir : "))
        h = t //3600
        r = t %  3600
        m = r // 60
        s = r % 60
        print(h, "H : ",m, "m : ",s,"s")
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide...")