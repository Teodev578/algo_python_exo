while True:
    try :
        note1 = float(input("Veuillez entrer votre première note : "))
        if(note1 >= 20):
            print("Veuillez entrer une note inférieur ou égale à 20")
            continue
        note2 = float(input("Veuillez entrer votre deuxième note : "))
        if(note2 >= 20):
            print("Veuillez entrer une note inférieur ou égale à 20")
            continue
        note3 = float(input("Veuillez entrer votre troisième note : "))
        if(note3 >= 20):
            print("Veuillez entrer une note inférieur ou égale à 20 recommençons")
            continue
        note4 = float(input("Veuillez entrer votre quatrième note : "))
        if(note4 >= 20):
            print("Veuillez entrer une note inférieur ou égale à 20")
            continue
        note5 = float(input("Veuillez entrer votre cinquième note : "))
        if(note5 >= 20):
            print("Veuillez entrer une note inférieur ou égale à 20")
            continue

        print("La somme des 5 notes est de : ", note1+note2+note3+note4+note5)
        print("La moyenne des notes est de : ", (note1+note2+note3+note4+note5)/5)
        break
    except ValueError:
        print("Veuillez entrer un nombre valide...")