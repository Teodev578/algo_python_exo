while True:
    try:
        note1=float(input("Veuillez entrer la première note de l'étudiant : "))
        note2=float(input("Veuillez entrer la première note de l'étudiant : "))
        note3=float(input("Veuillez entrer la première note de l'étudiant : "))
        moyenne=(note1+note2+note3)/3
        if moyenne < 10:
            print("Moyenne insuffisante")
            break
        elif moyenne >= 11 and moyenne <= 12:
            print("Moyenne : passable.")
            break
        elif moyenne > 12 and moyenne <= 14:
            print("Moyenne : Assez bien.")
            break
        elif moyenne > 14 and moyenne <= 16:
            print("Moyenne : bien.")
            break
        else:
            print("Moyenne : très bien.")
            break
    except ValueError:
        print("Erreur réessayez! Veuillez entrer un  nombre valide...")