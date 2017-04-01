from functions import *

def printFraction(l):
    s = ''
    return str(l[0]) + '/' + str(l[1])

def expantion(i,wanted):
    if i == 1 and i != wanted:
        f = expantion(i+1,wanted)
        return simplifySumOfFractions(1,1,f[1],f[0])
    if i == 1 and i == wanted:
        return simplifySumOfFractions(1,1,1,2)
    if i == wanted:
        return simplifySumOfFractions(2,1,1,2)
    
    f = expantion(i+1,wanted)
    return simplifySumOfFractions(2,1,f[1],f[0])

def expantionIt(wanted):
    r = [2,1]

    for x in range(1,wanted):
        r = simplifySumOfFractions(2,1,r[1],r[0])
    
    return simplifySumOfFractions(1,1,r[1],r[0])

def getExpation(wanted):
    return expantion(1,wanted)

end = 1000
counter = 0
for x in range(1,end+1):
    r = expantionIt( x )
    if nDigits(r[0]) > nDigits(r[1]):
        counter += 1
        print x,printFraction( r )

print counter