def chiffrement_cesar(input_text, shift_value):
    encrypted_text = ""
    for char in input_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift_value - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) + shift_value - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

def dechiffrement_cesar(encrypted_text_input, shift_value):
    return chiffrement_cesar(encrypted_text_input, -shift_value)

user_input_text = input("Entrez le texte : ")
shift = int(input("Entrez le décalage : "))
operation = input("Voulez-vous chiffrer (C) ou déchiffrer (D) : ").upper()

if operation == "C":
    result_text = chiffrement_cesar(user_input_text, shift)
    print("Texte chiffré:", result_text)
elif operation == "D":
    result_text = dechiffrement_cesar(user_input_text, shift)
    print("Texte déchiffré:", result_text)
else:
    print("Opération non reconnue. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")
