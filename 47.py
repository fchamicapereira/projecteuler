from functions import *

def consecutive(step):
    
    counter = 0
    n = 2
    x = 1

    while counter < step:
        if prime(n):
            x *= n
            counter += 1
        n += 1

    x -= step
    go = True

    while go:
        go = False
        x += 1
        divisors = []

        if len(list(set(primeDivisors(x)))) < step:
            go = True
            continue

        for i in range(0,step):
            divisors.append( list(set(primeDivisors( x + i )) ))
                
        for i in range(0,step-1):
            a = divisors[i]
            b = divisors[ i + 1 ]

            la = len( a )
            lb = len( b )

            if la < step or lb < step:
                go = True
                break

            intersect = list(set( a ).intersection( b ))

            if lb > la: max = lb
            else: max = la

            if len( intersect ) != max - step:
                go = True
                break

    return x

def check(x,step):
    print '\n--- checking %d ---\n' % x

    divisors = []

    for i in range(0,step):
        divisors.append( list(set(primeDivisors( x + i )) ))

    for i in range(0,step-1):
        a = divisors[i]
        b = divisors[ i + 1 ]

        la = len( a )
        lb = len( b )

        if la < step or lb < step:
            go = True
            break

        intersect = list(set( a ).intersection( b ))
        print x+i,x+i+1,a,b,intersect

    print '\n--- end of check ---\n'


consecutive(2)
consecutive(3)
consecutive(4)