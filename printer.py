import threading
import time

import signal
import sys

global exitFlag
global index
global final
global priterThreadId

def init():
    global exitFlag
    global index
    global final
    global printerThreadId

    exitFlag = 0
    index = 0
    final = 0

def signal_handler(signal, frame):
    global exitFlag
    exitFlag = 1
    print '\nKilled'
    sys.exit(0)

class myThreadPrinter (threading.Thread):
    def __init__(self, dt):
        threading.Thread.__init__(self)
        printerThreadId = threading.current_thread().ident
        self.name = "printer"
        self.dt = dt

    def run(self):
        print "-----Starting " + self.name + "-----"
        
        printer(self.dt)
        
        print "-----Exiting " + self.name + "-----"

def printer(dt):
    global exitFlag
    
    while 1:
        if exitFlag == 1:
            exit()
        time.sleep(1)
        print exitFlag
        if final != 0:
            print index,' (',100*float(index)/final,'% )'

def run(dt,main):
    global exitFlag
    signal.signal(signal.SIGINT, signal_handler)
   
    print "-----Starting main-----"

    init()

    p = myThreadPrinter(dt)

    p.start()

    try:
        main()
    except(KeyboardInterrupt, SystemExit):
        sys.exit()

    exitFlag = 1

    print "-----Exiting main-----"