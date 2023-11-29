import string

def construire_polybe(cle):
    cle = cle.upper()
    alphabet = string.ascii_uppercase.replace('J', '')
    cle_unique = ''.join(sorted(set(cle), key=cle.index))
    alphabet_restant = ''.join(sorted(set(alphabet) - set(cle_unique)))
    cle_complete = cle_unique + alphabet_restant

    polybe = [[0] * 5 for _ in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            polybe[i][j] = cle_complete[index]
            index += 1

    return polybe

def trouver_coordonnees(polybe, lettre):
    for i in range(5):
        for j in range(5):
            if polybe[i][j] == lettre:
                return i, j

def chiffrement_polybe(message, polybe):
    message_chiffre = ""
    for lettre in message:
        if lettre != ' ':
            i, j = trouver_coordonnees(polybe, lettre.upper())
            message_chiffre += str(i + 1) + str(j + 1) + ' '

    return message_chiffre.strip()

def dechiffrement_polybe(message_chiffre, polybe):
    coordonnees = [coord for coord in message_chiffre.split() if coord.isdigit()]
    message_dechiffre = ""
    
    for coord in coordonnees:
        i, j = int(coord[0]) - 1, int(coord[1]) - 1
        message_dechiffre += polybe[i][j]

    return message_dechiffre

def main():
    cle = input("Entrez la clé pour Polybe: ")
    message = input("Entrez le message: ")

    polybe_tableau = construire_polybe(cle)

    choix = input("Voulez-vous chiffrer ou déchiffrer? (chiffrer/déchiffrer): ").lower()

    if choix == "chiffrer":
        message_chiffre = chiffrement_polybe(message, polybe_tableau)
        print("Message chiffré:", message_chiffre)
    elif choix == "déchiffrer":
        message_dechiffre = dechiffrement_polybe(message, polybe_tableau)
        print("Message déchiffré:", message_dechiffre)
    else:
        print("Choix non valide. Veuillez choisir 'chiffrer' ou 'déchiffrer'.")

if __name__ == "__main__":
    main()
