#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

if __name__ == "__main__":

    for row in sys.stdin:
        dividir = row.split(",")
        segundaCol = dividir[3]
        terceraCol = dividir[4]

        sys.stdout.write(f"{segundaCol}\t{terceraCol}\n")
        
