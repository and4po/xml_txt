from fileinput import filename
import os
import shutil as sh

tipus = 0
subs = "."

ruta = input("Ruta: ")
arxiu = input("Arxiu(si vols convertir una carpeta deixa l'entrada buida): ")

ruta = ruta.replace('"', '')

# subs = input("Substitur(Sí/No): ")
# if subs == "Sí":
#     print("Good!")
# while subs != "Sí" or subs != "No" or subs != "":
#     print(subs)
#     print("No t'entenc, torna a internar-ho")
#     subs = input("Substitur(Sí/No): ")

if arxiu == "":
    if os.path.isdir(ruta) == True:
        tipus = 1
        filenames = os.listdir(ruta)
        os.mkdir(ruta + "/ArxiusTXT")
    else:
        print("La carpeta no existeix")
else:
    if os.path.isfile(ruta + "/" + arxiu) == True:
        tipus = 2
    else:
        print("L'arxiu no existeix")


if tipus == 1:
    for fn in filenames:
        if ".xml" in fn:
            nounom = fn.replace(".xml", ".txt")
            sh.copy2(ruta + "/" +fn, ruta + "/ArxiusTXT/" + nounom)
    print("Arxius convertits correctament!")
elif tipus == 2:
    nounom = arxiu.replace(".xml", ".txt")
    sh.copy2(ruta + "/" +arxiu, ruta + "/" + nounom)
    print("Arxiu convertit correctament!")
