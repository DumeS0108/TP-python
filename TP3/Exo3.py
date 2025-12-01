notes_str = input("Entrez les notes séparées par des espaces : ")

notes = [int(n) for n in notes_str.split()]

somme = 0
for n in notes:
    somme += n

moyenne = somme / len(notes)

print("La moyenne est :", moyenne)
