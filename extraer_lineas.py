"""
Apellidos : Ballester Navarro
Nombre : Teresa

Genera una programa que estraiga de forma aleatoria un porcentaje de las 
líneas de un fichero: se leen el fichero por líneas y se "tira un dado".
Si el dado es menor que el porcentaje la línea se graba en el fichero de 
salida. 

Con ese programa genera un fichero que se llame quijote_s05.txt
"""


import random
import sys

def main(filename, outfilename, ratio):
    with open(filename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} <infilename> <outfilename> <ratio>")
        exit(1)
    filename = sys.argv[1]
    outfilename = sys.argv[2]
    ratio = float(sys.argv[3])
    main(filename, outfilename, ratio)
