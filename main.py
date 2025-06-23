import random
import string

def afficher_bienvenue():
    print("Bienvenue dans le générateur de mot de passe sécurisé ! 🔐")

def demander_longueur():
    while True:
        try:
            longueur = int(input("Entrez la longueur souhaitée du mot de passe (Entre 4 et 15): "))
            if longueur < 4:
                print("La longueur doit être d'au moins 4 caractères.")
            if longueur > 15:
                print("La longueur ne doit pas dépasser 15 caractères.")
            else:
                return longueur
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def generer_mot_de_passe(longueur):
    # Caractères disponibles : lettres (majuscules et minuscules), chiffres et symboles
    lettres = string.ascii_letters  # a-zA-Z
    chiffres = string.digits        # 0-9
    symboles = "!$%"   # !$%

    # Fusionner tous les caractères possibles
    tous_caracteres = lettres + chiffres + symboles

    # Choisir aléatoirement des caractères
    mot_de_passe = ''.join(random.choice(tous_caracteres) for _ in range(longueur))
    return mot_de_passe

def main():
    afficher_bienvenue()
    longueur = demander_longueur()
    mot_de_passe = generer_mot_de_passe(longueur)
    print(f"Votre mot de passe généré est : {mot_de_passe}")

if __name__ == "__main__":
    main()