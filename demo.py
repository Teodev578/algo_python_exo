while True:
    t = int(input("Veuillez entrer le nombre de seconde que vous souhaitez convertir : "))

    if t < 0:
            print("⚠️ Erreur : Le nombre de secondes ne peut pas être négatif.\n")
            continue
    
    h = t // 3600
    