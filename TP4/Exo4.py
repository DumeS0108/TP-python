import pandas as pandasLib
import random


dataFrame = pandasLib.read_csv("donnervrai.csv")
X = dataFrame["vitesse"].tolist()
Y = dataFrame["danger"].tolist()


w = random.randint(-10, 10)
b = random.randint(-10, 10)


def Zpredict(x):
    z = w * x + b
    if z >= 0:
        return 1
    else:
        return 0


print(f"--- Paramètres : w={w}, b={b} ---")


for x, y_attendu in zip(X, Y):
    y_predit = Zpredict(x)
    erreur = y_attendu - y_predit
    
    # Affichage
    print(f"Vitesse: {x} | Attendu: {y_attendu} | Prédit: {y_predit} | Erreur: {erreur}")