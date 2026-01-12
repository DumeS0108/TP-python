import pandas as pandasLib

dataFrame1MonJeuDeDonneeDentrainement = pandasLib.read_csv("donnervrai.csv")

X = dataFrame1MonJeuDeDonneeDentrainement["vitesse"].tolist()
Y = dataFrame1MonJeuDeDonneeDentrainement["danger"].tolist()

print("Tableau X (Vitesse) :", X)
print("Tableau Y (Danger) :", Y)