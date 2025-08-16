try:
    nom = input("Veuillez saisir votre nom : ")
    if not nom.strip():
        raise ValueError("Le nom ne peut pas être vide.")
    
    age = int(input("Veuillez saisir votre âge : "))

    if age < 0:
        raise ValueError("L'âge doit être un nombre positif.")
    
    print("Bonjour",nom,", vous avez",age,"ans.")

except ValueError as e:
    print(f"Erreur : {e}")
    print("Erreur!! Veuillez entrer un nombre entier (•ᴗ•)\n")

except Exception as e:
    # Ce bloc attrape toutes les autres exceptions non prévues
    print(f"Une erreur inattendue est survenue : {e}")