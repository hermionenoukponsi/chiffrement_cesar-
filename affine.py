import math

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def trouver_inverse_modulaire(a, m):
    if pgcd(a, m) != 1:
        raise ValueError("Inverse modulaire n'existe pas pour les nombres non premiers entre eux.")
    
    _, x, _ = extended_gcd(a, m)
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def chiffrement_affine(message, a, b):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                message_chiffre += chr((a * (ord(lettre) - ord('A')) + b) % 26 + ord('A'))
            elif lettre.islower():
                message_chiffre += chr((a * (ord(lettre) - ord('a')) + b) % 26 + ord('a'))
        else:
            message_chiffre += lettre

    return message_chiffre

def dechiffrement_affine(message_chiffre, a, b):
    a_inverse = trouver_inverse_modulaire(a, 26)
    message_dechiffre = ""
    for lettre in message_chiffre:
        if lettre.isalpha():
            if lettre.isupper():
                message_dechiffre += chr((a_inverse * (ord(lettre) - ord('A') - b)) % 26 + ord('A'))
            elif lettre.islower():
                message_dechiffre += chr((a_inverse * (ord(lettre) - ord('a') - b)) % 26 + ord('a'))
        else:
            message_dechiffre += lettre

    return message_dechiffre

def main():
    choix = input("Voulez-vous chiffrer ou déchiffrer? (chiffrer/déchiffrer): ").lower()

    if choix not in ["chiffrer", "déchiffrer"]:
        print("Choix non valide. Veuillez choisir 'chiffrer' ou 'déchiffrer'.")
        return

    message = input("Entrez le message: ")
    a = int(input("Entrez la valeur de a: "))
    b = int(input("Entrez la valeur de b: "))

    if choix == "chiffrer":
        message_chiffre = chiffrement_affine(message, a, b)
        print("Message chiffré:", message_chiffre)
    else:
        message_dechiffre = dechiffrement_affine(message, a, b)
        print("Message déchiffré:", message_dechiffre)

if __name__ == "__main__":
    main()
