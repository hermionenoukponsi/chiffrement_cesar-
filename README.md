Le fichier chiffrement_cesar.py implémente le chiffrement et le déchiffrement du message selon le chiffrement cesar. Voici un bref aperçu du fonctionnement du code :

Chiffrement:
Prend en entrée un message et un décalage (par défaut, 3).
Déplace chaque lettre dans le message de 'décalage' positions vers la droite dans l'alphabet.
Les caractères non alphabétiques restent inchangés.
Retourne le message chiffré.

Déchiffrement:
Prend en entrée un message chiffré et un décalage.
Utilise la fonction de chiffrement avec un décalage négatif pour retrouver le message original.
Retourne le message déchiffré.

Programme Principal:
Demande à l'utilisateur s'il veut chiffrer ou déchiffrer un message.
Demande le message à l'utilisateur.
Effectue l'opération choisie (chiffrement ou déchiffrement) et affiche le résultat.


Le fichier affine.py implémente le chiffrement et le déchiffrement du message selon le chiffrement affine. Voici un bref aperçu du fonctionnement du code :

 Chiffrement:
   - Prend en entrée un message, une clé 'a', et une clé 'b'.
   - Pour chaque caractère alphabétique dans le message, applique la formule de chiffrement affine.
   - Formule : \(c \equiv (a \times p + b) \mod 26\), où \(c\) est le caractère chiffré, \(p\) est le caractère du message, et \(a\) et \(b\) sont les clés du chiffrement.
   - Retourne le message chiffré.

 Déchiffrement Affine:
   - Prend en entrée un message chiffré, une clé 'a', et une clé 'b'.
   - Calcule l'inverse multiplicatif modulaire de 'a'.
   - Applique la formule de déchiffrement affine : \(p \equiv a^{-1} \times (c - b) \mod 26\), où \(p\) est le caractère du message déchiffré et \(c\) est le caractère chiffré.
   - Retourne le message déchiffré.

Programme Principal:
Demande à l'utilisateur s'il veut chiffrer ou déchiffrer.
Prend le message et les clés 'a' et 'b' en entrée.
Appelle la fonction appropriée (chiffrement ou déchiffrement) et affiche le résultat.


Le fichier polybe.py implémente le chiffrement et le déchiffrement du message selon le chiffrement polybe. Voici un bref aperçu du fonctionnement du code :

Chiffrement:
La fonction prend en entrée un message et la grille de Polybe.
Elle parcourt chaque lettre du message (en ignorant les espaces) et trouve les coordonnées correspondantes dans la grille.
Les coordonnées sont concaténées sous forme de chaîne de caractères et espacées.
Le message chiffré est renvoyé.

Déchiffrement:
La fonction prend en entrée un message chiffré et la grille de Polybe.
Elle extrait les coordonnées du message chiffré.
Pour chaque paire de coordonnées, elle trouve la lettre correspondante dans la grille.
Les lettres sont concaténées pour former le message déchiffré, qui est renvoyé.

Programme Principal :
L'utilisateur entre une clé et un message.
La grille de Polybe est construite à partir de la clé.
L'utilisateur choisit s'il veut chiffrer ou déchiffrer.
Le résultat est affiché.

