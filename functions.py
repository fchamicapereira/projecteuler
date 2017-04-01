import math
import time
import collections 

def prime(n):
    if n <= 1:
        return False 
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6

    return True

def generatePrimes( limit ):
    n = 2
    primes = []

    while n <= limit:
        if prime(n):
            primes.append(n)
        n += 1

    return primes

def primeDivisors(n):
    list = []
    start = n

    if n <= 1:
        return []
    
    if not prime(n):
        start = int(math.sqrt(n))
    else:
        return [n]
    
    primes = generatePrimes(start)
    size = len(primes)
    i = size - 1
    p = primes[i]

    while i >= 0:
        p = primes[i]
        if n % p == 0:
            list.append(p)
            break
        i -= 1
    
    list.extend(primeDivisors(n/p))
    return list

def divisors(n):
    primes = primeDivisors(n)
    array = collections.Counter(primes).values()

    result = 1
    for x in array:
        result *= (x+1)

    return result


def palyndrome(n):
    digits = list(str(n))
    size = len(digits)
    
    for i in range(0,size/2):
        if digits[i] != digits[size-1-i]:
            return False
    return True

def simplify(a,b):
    aDivisors = primeDivisors(a)
    bDivisors = primeDivisors(b)

    inCommon = list(set(aDivisors) & set(bDivisors))

    for x in inCommon:
        if aDivisors.count(x) < bDivisors.count(x):
            limit = aDivisors.count(x)
        else:
            limit = bDivisors.count(x)
        
        for i in range(0,limit):
            aDivisors.remove(x)
            bDivisors.remove(x)
    
    p = 1
    for x in aDivisors: p *= x
    aFinal = p
    
    p = 1
    for x in bDivisors: p *= x
    bFinal = p

    return [aFinal,bFinal]

def simplify2(a,b):

    aDivisors = primeDivisors(a)
    bDivisors = primeDivisors(b)

    inCommon = list(set(aDivisors) & set(bDivisors))

    for d in inCommon:
        ca = aDivisors.count(d)
        cb = bDivisors.count(d)

        if ca < cb: c = ca
        else: c = cb

        for i in range(0,c):
            a /= d  
            b /= d

    
    return [a,b]

def simplifySumOfFractions(a,b,c,d):
    temp = b

    a *= d
    b *= d

    c *= temp
    d *= temp

    #result = simplify( a+c, d )

    #return [result[0],result[1]]
    return[a+c,d]

def digitsInCommon(x,y):
    a = map(int,str(x))
    b = map(int,str(y))
    return list(set(a) & set(b))

def repeatDigits(x):
    l = map(int,str(x))

    for d in l:
        if l.count(d) > 1:
            return True
    
    return False

def listOfDigits(x): return map(int,str(x))
def nDigits(x): return len(listOfDigits(x))
def fib(x):
    if x == 0: return 0
    if x == 1: return 1
    return fib(x-1) + fib(x-2)

def factorial(x):
    n = 1

    if x == 0: return 1

    while x != 1:
        n *= x
        x -= 1

    return n


def changeBase(number,base):
    result = ''
    next = number

    if base > 10:
        return 0
    
    if number == 0 or number == 1:
        return number
    
    if number < 0:
        return 0

    while next != 1:
        result = str(next % base) + result
        next = next / base

    return int('1' + result)

def pandigital(x,n):
    l = map(int,str(x))

    for x in range(1,n+1):
        if l.count(x) != 1:
            return False
    return True

def pandigitalZero(x,n):
    l = map(int,str(x))

    for x in range(0,n+1):
        if l.count(x) != 1:
            return False
    return True

def combinations(digit,number):
    size = len(number)
    result = []

    #if digit == '0':
    #    start = 1

    #else:
    start = 0

    for x in range(start,size+1):
        newN = number[:x] + digit + number[x:]
        result.append( newN )
    
    return result

def combinations2(number):
    n = list(str(number))
    
    size = len(n)
    result = []

    if size == 1:
        return [number]

    if size == 2:
        result = [n[0]+n[1],n[1]+n[0]]

    else:
        for i in range(0,size):
            s = ''

            for ii in range(0,size):
                if ii != i:
                    s = s + n[ii]

            r = combinations2( int(s) )
            
            for x in r:
                result.append( n[i] + str(x) )

    result = map(int,result)
    result = list(set(result))
    result.sort()
    
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
def printState(index,size):
    state = (index+1)*100.0/size
    state2 = int(str(state)[0])

    if state > 9 and process < state2:
        process = state2
        print 'State: %d/100' % state

    return process




def listToInteger(l):
    return int(''.join(map(str,l)))



def functionDuration(f):
    startTime = time.time()
    f()
    print str(time.time() - startTime) + ' sec'
def reverseNumber(n):
    l = map(int,str(n))
    l.reverse()
    return listToInteger(l)
def cyclicList(l):
    for x in l:
        if nDigits(x) < 4:
            return False
    
    size = len(l)
    l = map(str,l)

    for term in range(0,size):
        nextTerm = (term+1) % size
        
        if l[term][2:] != l[nextTerm][:2]:
            return False

    return True

def first2DigitsInList(twoDigits,l):
    l = map(str,l)
    result = []

    for term in l:
        if term[:2] == twoDigits:
            result.append( term )
    
    return result
def sPermutations(s):
    def aux(c,s):
        size = len(s)
        result = []

        for p in range(0,size + 1):
            result.append( s[:p] + c + s[p:] )
                
        return result

    if len(s) == 1:
        return s[0]

    if len(s) == 2:
        return [s[0]+s[1],s[1]+s[0]]
    
    cS = list(s)
    size = len(s)
    i = size - 1
    result = [cS[ i ]]
    wantedS = 2
    
    while len( result[0] ) != size:
        i -= 1

        while len( result[0] ) != wantedS:
            term = result.pop(0)
            result.extend( aux(cS[i],term) )
        
        wantedS += 1

    return result
def genCubeRoot( digits ):
    result = []

    x = 1
    while 1:
        n = x**3
        d = nDigits( n )

        if d < digits:
            x += 1
            continue

        if d > digits:
            return result
        
        result.append( n )
        x += 1

    return result

def isComb(n1,n2):
    n1 = str(n1)
    n2 = str(n2)

    for n in n2:
        if n not in n1:
            return False
        
        if n2.count( n ) != n1.count( n ):
            return False
    
    return True

#polygonal numbers
def triangle(n): return int(0.5*n*(n+1))
def square(n): return n*n
def pentagonal(n): return n*(3*n-1)/2
def hexagonal(n): return n*(2*n-1)
def heptagonal(n): return n*(5*n-3)/2
def octagonal(n): return n*(3*n-2)

#polygonal n digits generators (substitute function for 
# polygonal function on call)
def generateNDigitsPolygonal(digits,function):
    numbers = []
    n = 1

    while 1:
        afterF = function(n)
        d = nDigits( afterF )

        if d > digits:
            break
        
        if d == digits:
            numbers.append( afterF )
        
        n += 1
    
    return numbers

#check polygonal numbers
def isTriangle(x):
    x = 2*x
    digits = nDigits(x)

    if digits % 2 == 0:
        end = pow(10, (digits / 2))
    else:
        end = pow(10,( digits + 1 ) /2)

    n = 1

    while n < end:
        if n*(n+1) == x:
            return n
        n += 1

    return -1
def checkIfPentagonal(x):
    xDigits = nDigits(x)

    if xDigits % 2 == 0:
        nDigitsLimit = xDigits/2 
    else:
        nDigitsLimit = (xDigits+1)/2

    
    if nDigitsLimit > 1:
        start = pow(10,nDigitsLimit-2)*8
    else:
        start = pow(10,nDigitsLimit-1)

    end = pow(10,nDigitsLimit)

    for n in range(start,end):
        if pentagonal(n) == x:
            return n
    
    return -1