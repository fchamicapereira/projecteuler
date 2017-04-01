from functions import *
import signal
import time

def arrange(primes,number):
    n = map(int,str(number))
    size = len(n)

    for group in range(1,size):
        print 'dumb'

def printArray(array):
    s = ''

    for a in array:
        s = s +  str(a) + ' '

    print s


#lista de 0 e 1, sendo 1 os marcados para substituicao
def pull(l):
    size = len(l)
    firstPuller = 0
    pullers = 0

    if l[ size-1 ] == 0:
        for i in range(size-2,0,-1):
            if l[i] == 1:
                l[i] = 0
                l[i+1] = 1

                return l

    ones = l.count(1)

    for i in range(size-1, 0, -1):
        if l[i] == 0:
            firstPuller = i+1
            break

        pullers += 1

    if firstPuller == 0 or firstPuller == size - ones:
        return []

    for i in range(firstPuller-1,-1,-1):

        if l[i] == 1:
            l[i] = 0
            l[i+1] = 1

            i += 2

            counter = 0
            for p in range(0,pullers):
                l[i] = 1
                i += 1
            
            for r in range(i,size):
                l[r] = 0

            break
    
    return l

def replaceOnes(array,number):
    size = len(array)
    n = map(int,str(number))
    result = []

    for digit in range(0,10):
        temp = list(n)

        for i in range(0,size):
            if array[i] == 1:
                temp[i] = digit
        

        nTemp = listToInteger( temp )
        
        if len(str(nTemp)) != size: continue

        if prime(nTemp):
            result.append( nTemp )
        

    return result

def giveStartingArray(number,group):
    size = len(str(number))
    array = [0] * size

    if group >= size:
        print 'grupo maior que o numero: n=',number,'g=',group
        return []

    for x in range(0,group):
        array[x] = 1
    
    return array


def combinations( number, objective ):
    size = len(str(number))

    for group in range(1,size):
        array = giveStartingArray(number,group)
        temp = []

        while array != []:    
            temp.append( list(array) )
            array = pull(array)
        
        for a in temp:
            result = replaceOnes( a, number )
            
            if len(result) >= objective:
                print 'Number',number   
                print 'Combination' 
                printArray(a)
                print 'result',result
                print 'Length',len( result ),'\n'

                return False
    return True

global x 
global dt

dt = 15

def handler(signum, frame):
    global x
    global dt

    print 'Signal handler called with signal', signum
    print 'x =',x
    signal.alarm(dt)

def main():
    global x
    global dt

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(dt)

    x = 56003
    objective = 8
    condition = True

    while condition:
        if prime(x):
            condition = combinations( x, objective )
        x += 2

functionDuration(main)