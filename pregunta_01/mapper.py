#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

if __name__ == "__main__":

    for row in sys.stdin:
        dividir = row.split(",") 
        segundaCol = dividir[2]
   
        sys.stdout.write("{}\t1\n".format(segundaCol))
    
