from functions import *

def main():
    exist = True
    power = 0
    result = []

    while exist:
        exist = False
        x = 1
        power += 1

        p = pow(x,power)
        digits = nDigits( p )

        while digits <= power:
            if digits == power:
                exist = True
                result.append( p )
                print x,p,'power',power

            x += 1
            p = pow(x,power)
            digits = nDigits( p )

    print len( result )
main()