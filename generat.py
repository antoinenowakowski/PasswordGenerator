import random

NombreDeCaracteres = int(input("Combien de caractères ? "))

liste = ["a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m","n", "o","p", "q","r", "s","t", "u","v", "w","x", "y","z", "-", "_", ";",",", ".","!", "*", "#", "{", "(", "[", "`", "'", ")", "]", "}",0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def ChoisitAletoirementUnCaractere():
    Caracteres = random.choice(liste)
    return Caracteres

EstDifferentsDuNombreChoisit = 0

PasswordEnListe = []
while EstDifferentsDuNombreChoisit != NombreDeCaracteres:
    Password = ChoisitAletoirementUnCaractere()
    PasswordEnListe.append(Password)
    EstDifferentsDuNombreChoisit+=1

FinalPassword = "".join(map(str, PasswordEnListe))
print(FinalPassword)