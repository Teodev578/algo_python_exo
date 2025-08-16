import random

# On génère le nombre à deviner une seule fois, au début.
chiffre = random.randint(1, 30)
essais_max = 5

print("Bienvenue dans le jeu de devinette ! Devine un nombre entre 1 et 30.")

# On utilise une boucle for pour limiter le nombre d'essais.
for i in range(essais_max):
    try:
        n = int(input(f"Il te reste {essais_max - i} essais. Saisis un nombre : "))

        if n < 1 or n > 30:
            print("Le nombre doit être entre 1 et 30. Réessaie.")
            continue  # Permet de passer à l'itération suivante sans compter cet essai

        # Logique simplifiée pour guider le joueur.
        if n < chiffre:
            print("C'est plus grand.")
        elif n > chiffre:
            print("C'est plus petit.")
        else:
            # Si le nombre est bon
            print(f"Trouvé !! Le nombre était bien {chiffre}.")
            break  # On sort de la boucle for
    
    except ValueError:
        print("Erreur!! Veuillez entrer un nombre entier (•ᴗ•)\n")
        # On ne met pas de break ici pour laisser le joueur retenter.
        continue

# Ce bloc s'exécute si la boucle for se termine sans break (le joueur a perdu)
else:
    print(f"Désolé, tu as épuisé tous tes essais. Le nombre à trouver était {chiffre}.")