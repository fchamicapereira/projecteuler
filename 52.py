from functions import *
import signal

def sameDigits(n1,n2):
    if len(str(n1)) != len(str(n2)): return False
    return len( list( set(str(n1)) & set(str(n2)) ) ) == len(str(n1))


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

    x = 1
    condition = True
    start = 2
    end = 7

    while condition:
        condition = False

        x += 1

        for i in range(start,end):
            if sameDigits(x,i*x) == False:
                condition = True
                break
    
    print x


functionDuration(main)
