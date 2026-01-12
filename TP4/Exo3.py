import pandas as pandasLib
import random

dataFrame1MonJeuDeDonneeDentrainement = pandasLib.read_csv("donnervrai.csv")
X = dataFrame1MonJeuDeDonneeDentrainement["vitesse"].tolist()
Y = dataFrame1MonJeuDeDonneeDentrainement["danger"].tolist()

w = random.randint(-10, 10)
b = random.randint(-10, 10)
print(f"Initialisation -> w: {w}, b: {b}")

def Zpredict(x):
    z = w * x + b
    if z >= 0:
        return 1
    else:
        return 0


print("--- Test des prédictions ---")
for x in X:
    print(f"x = {x}, prédiction = {Zpredict(x)}")