import random

nombre_secret = random.randint(1,50)
tentatives = 0

print("Jeu de devinette")

print("J'ai choisi un nombre entre 1 et 50")
print("Essaie de le deviner !")

while True:
    try:
        choix = int(input("Entrez un nombre: "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    tentatives += 1

    if choix < nombre_secret:
        print("Trop petit")
    elif choix > nombre_secret:
        print("Trop grand")
    else:
        print(f"Bravo! Tu as trouvé le nombre en {tentatives} tentatives.")
        break.py
