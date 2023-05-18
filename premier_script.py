import os
chemin_dossier = input("Entrez le chemin du dossier : ") 
dossier_existe = os.path.isdir(chemin_dossier)
print(dossier_existe)