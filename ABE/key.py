import re
import os
import sys

argv=[]
for arg in sys.argv:
    argv.append(arg)

if (len(argv)!=3):
    print("ERROR : Not enough arguments - Please retry with attributes' file and user's name.")
# Ouvrir le fichier en lecture seule
else:
    file = open(argv[1], "r")
    listeAttributs = []
    for line in file:
        #tab.extend(
        attribut=line.split("\n")
        #print(x)
        listeAttributs.append(attribut[0])


    Attributs="|".join(listeAttributs)
    print(Attributs)
    file.close()


    print("----------------------------------------------------")
    print("---------------GENERATING USER'S KEY----------------")
    print("--------------Attributes : "+argv[1]+"--------------")
    print("----------------------------------------------------")

    os.system('./oabe_keygen -s CP -p org1 -i "'+ Attributs +'" -o '+argv[2]+'CPABE')
    #print('./oabe_keygen -s CP -p org1 -i "'+ Attributs +'" -o '+argv[2]+'CPABE')
    print("Generate key for "+argv[2])