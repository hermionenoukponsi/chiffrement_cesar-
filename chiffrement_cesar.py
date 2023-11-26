def chiffrement_cesar(message, decalage=3):
    message_chiffre = ""

    for caractere in message:
        if caractere.isalpha():
            # Gestion des lettres majuscules
            if caractere.isupper():
                message_chiffre += chr((ord(caractere) - ord('A') + decalage) % 26 + ord('A'))
# Gestion des lettres minuscules
            else:
                message_chiffre += chr((ord(caractere) - ord('a') + decalage) % 26 + ord('a'))
        else:
            message_chiffre += caractere

    return message_chiffre
def dechiffrement_cesar(message_chiffre, decalage=3):
return chiffrement_cesar(message_chiffre, -decalage)

# Demander à l'utilisateur s'il veut chiffrer ou déchiffrer
choix = input("Voulez-vous chiffrer ou déchiffrer un message? (chiffrer/déchiffrer): ").lower()

# Demander le message à l'utilisateur
message_original = input("Entrez le message : ")
# Si l'utilisateur veut chiffrer
if choix == "chiffrer":
    message_chiffre = chiffrement_cesar(message_original)
    print("Message chiffré:", message_chiffre)
# Si l'utilisateur veut déchiffrer
elif choix == "déchiffrer":
message_dechiffre = dechiffrement_cesar(message_original)
    print("Message déchiffré:", message_dechiffre)
else:
    print("Choix non valide. Veuillez choisir 'chiffrer' ou 'déchiffrer'.")
