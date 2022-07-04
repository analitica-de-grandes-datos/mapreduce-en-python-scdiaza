#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == '__main__':
    curkey = None
    total = 0
    max = 0
    aux = 0
    
    for line in sys.stdin:        
        key, val = line.split("\t")
        val = int(val)
        aux = val

        if key == curkey:
            if aux > max:
                max = aux  
        else:          
            if curkey is not None:
              
                sys.stdout.write("{}\t{}\n".format(curkey, max))
            curkey = key
            max = val

    sys.stdout.write("{}\t{}\n".format(curkey, max))
