from functions import *
import time

def primeGenerator(n):
    i = 0
    result = []
    counter = 2

    while i < n:
        if prime(counter):
            i += 1
            result.append(counter)
        
        counter += 1

    return result


def condition(primes,n):
    number = map(str,str(n))
    digits = len(number)
    i = 1

    while i + 2 < digits:
        temp = number[i] + number[i+1] + number[i+2]
        
        if int(temp) % primes[i-1] != 0:
            return False

        i += 1
    
    return True

def missingDigits(n):
    result = []
    number = map(str,str(n))

    for x in range(0,10):
        if number.count(str(x)) == 0:
            result.append(str(x))

    return result

def combinations(digit,number):
    size = len(number)
    result = []

    if digit == '0':
        start = 1

    else:
        start = 0

    for x in range(start,size+1):
        result.append( number[:x] + digit + number[x:] )
    
    return result

def pandigitalGenerator(digits):
    end = digits-1
    
    print '\n----Generating 0 to %d pandigitals----\n' % end
    
    result = [str(end)]

    expected = float(end*factorial(end))
    print 'expected %d pandigitals\n' % int(expected)

    process = 0
    digit = 1

    for x in range(end-1,-1,-1):

        print 'adding digit %d' % x

        while digit < digits-x:
            result.extend( combinations(str(x), result.pop(0) ) )
            digit = len(result[0])

            size = len(result)
            state = int(100*size/expected)

            if state > 9 and int(str(state)[0]) > process:
                process = int(str(state)[0])
                print '---state update: %d/100' % state

        print 'COMPLETE (%d digits)\n' % (len(result[0]))

    print 'mapping...'
    result = map(int,result)
    print 'sorting...'
    result.sort()
    print '\ntotal: %d' % len(result)

    print '\n----Generation complete----\n'

    return result

primes = primeGenerator(7)

startTime = time.time()
pandigitalList = pandigitalGenerator(10)
print str((time.time() - startTime) / 60) + ' min'

print '1406357289 esta na lista? ' + str(1406357289 in pandigitalList)
print 'satisfaz a condicao? ' + str(condition(primes,1406357289))

sum = 0
for n in pandigitalList:
    if condition(primes,n):
        print 'found %d' % n
        sum += n

print sum