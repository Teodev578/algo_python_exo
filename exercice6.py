notes = []
nombre_notes_a_saisir = 5

while len(notes) < nombre_notes_a_saisir:
    try:
        note_actuelle = float(input(f"Veuillez entrer la note {len(notes) + 1} : "))

        # Vérification si la note est valide
        if note_actuelle < 0 or note_actuelle > 20:
            print("⚠️ Erreur : La note doit être comprise entre 0 et 20.")
            continue # Passe à l'itération suivante de la boucle

        notes.append(note_actuelle) # Ajoute la note à la liste si elle est valide

    except ValueError:
        print("⚠️ Erreur : Veuillez entrer un nombre valide.")

# Après la boucle, les calculs sont faits sur la liste
somme = sum(notes)
moyenne = somme / nombre_notes_a_saisir

print(f"\n✅ La somme des {nombre_notes_a_saisir} notes est de : {somme}")
print(f"✅ La moyenne des notes est de : {moyenne}")