#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys

if __name__ == "__main__":

    for line in sys.stdin:

        atributo, valor = line.split('\t')
        valor = list(valor.split(','))

        for letra in valor:
            sys.stdout.write(
                "{}-{}\n".format(letra.strip(), atributo.zfill(4)))
            
