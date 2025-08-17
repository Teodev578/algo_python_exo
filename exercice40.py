
#ici j'ai retirer la boucle while tru: car celà créais un erreur python.
try:
    n = int(input("Entrez un nombre entier: "))
    nbr = 0
    if n < 0:
        print("Erreur: Le nombre doit être positif.")
        
    while n !=0:
        n = n // 10
        nbr = nbr + 1
    print(f"Le nombre total de chiffres dans le nombre {n} est : {nbr}")

except ValueError:
    print("Oops... On dirait que vous n'avez pas entrer un nombre valide.\n")