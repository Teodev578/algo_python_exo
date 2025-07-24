import datetime

try:
    annee_naissance = int(input("Veuillez entrer votre année de naissance : "))
    annee_actuelle = datetime.datetime.now().year
    age = annee_actuelle - annee_naissance
    print(f"Votre âge est de {age} ans cette année.")
except ValueError:
    print("Entrée invalide. Veuillez entrer une année valide (un nombre entier).")
