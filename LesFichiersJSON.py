import json

chemin_fichier = r"C:\Users\pablo\Documents\nouveaux projets 2023\Python\liste.txt"

# fichier = open(chemin_fichier, "r")
# contenu_fichier = fichier.read()
# fichier.close()
# print(contenu_fichier)

# with open(chemin_fichier, "w") as f:
#     f.write("Mais en ete seulement")

with open(chemin_fichier, "w") as f:
    json.dump([1, 2, 3, 4, 5], f)

with open(chemin_fichier, "r") as f:
    ma_liste = json.load(f)

ma_liste.append(6)

with open(chemin_fichier, "w") as f:
    json.dump(ma_liste, f)