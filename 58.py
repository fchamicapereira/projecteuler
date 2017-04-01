from functions import *

def checkDiagonal( obj ):
    primeDiagonalCounter = 3
    diagonalCounter = 5
    length = 2
    x = 9
    p = int(round(100.0*primeDiagonalCounter/diagonalCounter,0))


    while p >= obj:
        x += 1
        length += 1

        for i in range(0,4):
            x += length

            if i == 0:
                length += 1

            if prime(x):
                primeDiagonalCounter += 1

            diagonalCounter += 1

        p = 100.0*primeDiagonalCounter/diagonalCounter
        
    print ("Length %d") % (length + 1)
    print ("Primes in diag: %f/100 ( %d / %d )") % (p,primeDiagonalCounter,diagonalCounter)
    print 'Last digit:',x

checkDiagonal(10)