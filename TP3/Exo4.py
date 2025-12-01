# Définition de la fonction
def maximum_de_trois(a, b, c):
    return max(a, b, c)

# Programme principal
x = int(input("Entrez le premier nombre : "))
y = int(input("Entrez le deuxième nombre : "))
z = int(input("Entrez le troisième nombre : "))

max_val = maximum_de_trois(x, y, z)
print("Le maximum est :", max_val)
