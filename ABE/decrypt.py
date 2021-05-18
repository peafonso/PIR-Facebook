import re
import os
import sys

argv=[]
for arg in sys.argv:
    argv.append(arg)

if (len(argv)!=3):
    print("ERROR : Not enough arguments - Please retry with encrypted file and user' name.")
# Ouvrir le fichier en lecture seule
else:
    print("----------------------------------------------------")
    print("----------------------DECRYPT-----------------------")
    print("----------------------------------------------------")

    os.system('./oabe_dec -s CP -p org1 -k '+argv[2]+'CPABE.key -i '+argv[1]+' -o plainOK.'+argv[1])
    #print('./oabe_dec -s CP -p org1 -k '+argv[2]+'CPABE.key -i '+argv[4]+'.cpabe -o plainFail.'+argv[4])
    try: 
        file = open('plainOK.'+argv[1], "r")
        print("Decrypted successfully")
    except FileNotFoundError:
        print("Decrypted unsuccessfully")