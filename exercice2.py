import datetime

try:
    annee_naissance = int(input("Veuillez entrer votre année de naissance : "))
    if not annee_naissance.strip():
        raise ValueError("L'année de naissance ne peut pas être vide.")
    
    annee_actuelle = datetime.datetime.now().year
    age = annee_actuelle - annee_naissance
    print(f"Votre âge est de {age} ans cette année.")

except ValueError as e:
    print(f"Erreur : {e}")
    print("Veuillez entrer un nombre entier (•ᴗ•)\n")

except Exception as e:
    # Un filet de sécurité pour les erreurs imprévues
    print(f"Une erreur inattendue est survenue : {e}")