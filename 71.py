from functions import *
import signal
from operator import itemgetter

global d 
global dt
global frac

dt = 15

def handler(signum, frame):
    global x
    global dt

    print 'Signal handler called with signal', signum
    print 'd =',d,'\nwinner so far:',fracToString( frac )
    signal.alarm(dt)

def fracToString(frac):
    return str( frac[0] ) + '/' + str( frac[1] )

def printlist( l ):
    size = len(l)
    t = ''

    x = 0
    while x < size:
        t += l[x][1] + ' '

        x += 1

    print t

def printWanted( l, wanted ):
    size = len(l)
    t = ''

    x = 0
    while x < size - 1:
        if l[x+1][1] == wanted:
            print l[x][1]
            return

        x += 1

def main():
    global d
    global dt
    global frac

    limit = 1000000

    d = 2

    winnerN = 0
    winnerDiff = 1
    frac = [0,1]

    CONSTANT = 3.0/7

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(dt)

    while d <= limit:
        start = int( float( frac[0] ) * d / frac[1] )
        end = int( 3.0*d/7 ) + 1

        for n in range(start,end):
            result = float(n)/d

            if result >= CONSTANT:
                break

            diff = CONSTANT - result 

            if  diff < winnerDiff:
                if n == 3 and d == 7:
                    continue

                frac = simplify(n,d)

                winnerDiff = diff
                winnerN = result
            
        d += 1

    print fracToString( frac )

functionDuration( main )