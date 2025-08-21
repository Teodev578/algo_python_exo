
#ici j'ai retirer la boucle while tru: car celà créais un erreur python.
try:
    n = int(input("Entrez un nombre entier: "))
    inverse = 0
    if n < 0:
        print("Erreur: Le nombre doit être positif.")
        
    while n !=0:
        inverse = (inverse*10) + (n%10)
        n = n //10
    print(f"L'inverse de {n} est : {inverse}")

except ValueError:
    print("Oops... On dirait que vous n'avez pas entrer un nombre valide.\n")