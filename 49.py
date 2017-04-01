from functions import *

def isSequence(l,minimum):
    l.sort()
    d = []
    size = len(l)
    seq = []

    minimum -= 1
    
    if size < minimum:
        return -1

    for a in range(size-1,minimum-2,-1):
            for b in range(a-1,-1,-1):
                    temp = l[a]-l[b]
                    d.append(temp)

    for x in d:
        if d.count(x) == minimum:
            return x
    
    return -1

def getSequence(l,minimum):
    l.sort()
    size = len(l)
    seq = []
    d = isSequence(l,minimum)

    if d == -1:
        return []

    a = size-1
    special = False
    
    for a in range(size-1,1,-1):
        temp = l[a]-l[a-1]
        
        if temp == d:
            seq.append(l[a])
            seq.append(l[a-1])


    if len(seq) < minimum: return []

    
    
    seq = list(set(seq))
    seq.sort()

    diff = []
    for i in range(0,len(seq)-1):
        diff.append( seq[i+1] - seq[i] )
        
        
    if diff.count(diff[i]) == minimum - 1 and len(diff) == minimum - 1:
        return seq
       
    return []

start = 1000
end = 10000
N = end - start
                           
checked = [0] * N
    
for x in range(start,end):
    if prime(x) and checked[x-start] == 0:
        comb = combinations2(x)

        primes = []
        
        for n in comb:
            checked[n-start] = 1
            if prime(n):
                primes.append(n)
        
        sequence = getSequence(primes,3)
        if sequence != []:
            print sequence
            d = []
            for i in range(0,len(sequence)-1):
                d.append( sequence[i+1] - sequence[i] )
            print "Difference: " + str(d)
