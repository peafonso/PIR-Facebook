import re
import os
import sys



argv=[]
for arg in sys.argv:
    argv.append(arg)

if (len(argv)!=3):
    print("ERROR : Not enough arguments - Please retry with not encrypted file and cypher attributes.")
# Ouvrir le fichier en lecture seule
else:
    print("----------------------------------------------------")
    print("----------------------ENCRYPT-----------------------")
    print("----------------------------------------------------")
    os.system('./oabe_enc -s CP -p org1 -e "'+argv[2]+'" -i '+argv[1]+' -o '+argv[1]+'.cpabe')
    print('./oabe_enc -s CP -p org1 -e "'+argv[2]+'" -i '+argv[1]+' -o '+argv[1]+'.cpabe')

    print("Encryted successfully")