import re
import os
import sys

argv=[]
for arg in sys.argv:
    argv.append(arg)


# Ouvrir le fichier en lecture seule
file = open(argv[1], "r")
listeAttributs = []
for line in file:
    #tab.extend(
    attribut=line.split("\n")
    #print(x)
    listeAttributs.append(attribut[0])


print("|".join(listeAttributs))
file.close()

#os.system('./oabe_setup -s CP -p org1')
print("Generate system parameters for CP")

os.system('./oabe_keygen -s CP -p org1 -i "'+ "|".join(listeAttributs) +'" -o '+argv[2]+'CPABE')
print('./oabe_keygen -s CP -p org1 -i "'+ "|".join(listeAttributs) +'" -o '+argv[2]+'CPABE')
print("Generate key for "+argv[2])


if(argv[3]=="-d"):
    print("-------------------DECRYPT-------------------")
    os.system('./oabe_dec -s CP -p org1 -k '+argv[2]+'CPABE.key -i '+argv[4]+'.cpabe -o plainOK.'+argv[4])
    print('./oabe_dec -s CP -p org1 -k '+argv[2]+'CPABE.key -i '+argv[4]+'.cpabe -o plainFail.'+argv[4])


elif(argv[3]=="-e"):
    print("-------------------ENCRYPT-------------------")
    
    os.system('./oabe_enc -s CP -p org1 -e "'+argv[5]+'" -i '+argv[4]+' -o '+argv[4]+'.cpabe')
    print('./oabe_enc -s CP -p org1 -e "'+argv[5]+'" -i '+argv[4]+' -o '+argv[4]+'.cpabe')

