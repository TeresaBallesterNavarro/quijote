"""
Apellidos : Ballester Navarro
Nombre : Teresa

Haz un programa de contar palabras y pruébalo con el fichero quijote_s05.txt.
Copia la salida y ponla en un fichero llamado out_quijote_s05.txt
Prueba el programa con el libro completo.
Copia la salida en un fichero llamado out_quijote.txt
"""

from pyspark import SparkContext
import sys


def words(filename, outfilename):
    
    with SparkContext() as sc: #para asegurar que el contexto spark se cierra correctamente
        sc.setLogLevel("ERROR")
        data = sc.textFile(filename)
        words_rdd = data.map(lambda x: len(x.split())) #se divide cada línea en palabras
        words = words_rdd.collect()
        suma = words_rdd.sum()
        
        with open(outfilename, 'w') as outfile:
            outfile.write('Número total de palabras en el texto:')
            outfile.write('\n')
            outfile.write(str(suma))
    
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 {0} <file>".format(sys.argv[0]))
    
    filename = sys.argv[1]
    outfilename = sys.argv[2]
    words(filename, outfilename)
