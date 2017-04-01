from functions import *
import printer

def main():
    end = pow(10,6)

    primes = []

    for x in range(2,end):
        if prime(x):        
            primes.append(x)

    for p in primes:
        if p > end/2:
            marker = primes.index(p)
            break

    size = len(primes)

    sum = 0
    counter = 0

    recordLen = 0
    recordSum = 0

    remember = -1

    printer.final = marker+1

    print 'Starting routine'
    for x in range(0,marker+1):

        sum = 0
        counter = 0
        remember = -1

        printer.index = x
        
        for y in range(x,marker+1):
            
            sum += primes[y]

            if sum > end:
                break

            if sum not in primes:
                if remember == -1:
                    remember = y
                continue

            counter += 1

            if remember != -1:
                counter += y - remember
                remember = -1

            if counter > recordLen:
                recordSum = sum
                recordLen = counter

    print recordSum,recordLen

printer.run(20,main)
#main()