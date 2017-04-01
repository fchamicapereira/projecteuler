from functions import *

def isCubeRoot( n ):
    return int( round( n ** (1./3) ) ) ** 3 == n

def cleanListPermut( n ):
    listPermut = list(set( sPermutations( str(n) ) ) )
    size = len( listPermut )
    i = 0
   
    while i < size:
        if listPermut[i][0] == '0':
            listPermut.pop(i)
            size -= 1
            i -= 1
        i += 1

    listPermut = map(int, listPermut)

    return listPermut



def main():   
    counterMax = 5
    digits = 1

    while 1:
        cuberoots = genCubeRoot( digits )
        size = len( cuberoots )
        print 'len of cuberoots of',digits,'digits:',size

        for cr in cuberoots:
            comb = [cr]
            start = cuberoots.index( cr )
            
            for i in range(start,size):
                if isComb(cr, cuberoots[i]):
                    comb.append( cuberoots[i] )
            
            inter = set( cuberoots ) & set( comb )
            counter = len( inter )

            if counter == counterMax:
                print cr,inter
                exit(1)
        digits += 1
        
main()