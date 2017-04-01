from functions import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

global cards
global winnerHands

winnerHands = [ 'High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush' ]
cards = [ '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A' ]

def printHand( hand ):
    hand = sort(hand)
    s = ''

    for c in hand:
        if 'H' in c or 'D' in c:
            temp = bcolors.FAIL
        else:
            temp = ''
        s = s + temp + c + ' ' + bcolors.ENDC

    
    return s

def printPlay( play ):
    return play[0] + ' (' + play[1] + ')'


def sort(hand):
    global cards
    handSorted = []
    result = []

    for c in hand:
        newValue = cards.index( c[0] )   
        handSorted.append( [newValue,c[1]] )

    handSorted.sort( key = lambda x: x[0] )

    for i in range(0,len(handSorted)):
        cardValue = cards[ handSorted[i][0] ]
        result.append( cardValue + handSorted[i][1] )
        
    return result

def playInHand(hand):
    
    def royalFlush(hand):
        global cards

        t = ''
        i = cards.index('T')

        for c in hand:
            if len(t) == 0:
                t = c[1]

            if c[0] != cards[ i ] or c[1] != t:
                return ''

            i += 1
        
        return 'T'
    
    def straightFlush(hand):
        if len(flush(hand)) == 0:
            return ''

        return straight(hand)

    def fourKind(hand):
        global cards
        values = []

        for c in hand:
            values.append( c[0] )

        for v in values:
            if values.count(v) == 4:
                return v
        
        return ''

    def fullHouse(hand):
        global cards
        values = []
        threeK = threeKind( hand )

        if threeK == '':
            return threeK

        for c in hand:
            values.append( c[0] )
        
        i = 0

        for v in values:
            if values.count( v ) == 2 and v != threeK:
                return threeK
        
        return ''

    def flush(hand):
        global cards
        types = []

        for c in hand:
            types.append( c[1] )

        if types.count( types[0] ) == 5:
                return highCard(hand)
        
        return ''

    def straight(hand):
        global cards

        i = -1

        for c in hand:

            if i == -1:
                i = cards.index( c[0] )

            if c[0] != cards[ i ]:
                return ''

            i += 1
        
        return hand[0][0]

    def threeKind(hand):
        global cards

        values = []

        for c in hand:
            values.append( c[0] )
        
        for v in values:
            if values.count(v) == 3:
                return v

        return ''

    def twoPairs(hand):
        global cards

        values = []

        for c in hand:
            values.append( c[0] )
        
        counter = 0
        i = 0
        max = ''

        for v in values:
            if values.count( v ) == 2 and v not in max:
                max += v + ' '
        
        if len(max) == 4:
            return max[:len(max)-1]
        
        return ''

    def onePair(hand):
        global cards

        values = []

        for c in hand:
            values.append( c[0] )
        
        
        for v in values:
            if values.count( v ) == 2:
                return v
        
        return ''

    def highCard(hand):
        return hand[ len(hand) - 1 ][0]

    global winnerHands

    handSorted = sort(hand)

    i = len(winnerHands) - 1

    for x in range(i,0,-1):
        if x == 9:
            result = royalFlush( handSorted )
        elif x == 8:
            result = straightFlush( handSorted )
        elif x == 7:
            result = fourKind( handSorted )
        elif x == 6:
            result = fullHouse( handSorted )
        elif x == 5:
            result = flush( handSorted )
        elif x == 4:
            result = straight( handSorted )
        elif x == 3:
            result = threeKind( handSorted )
        elif x == 2:
            result = twoPairs( handSorted )
        elif x == 1:
            result = onePair( handSorted )
        
        if len(result) != 0:
            return [winnerHands[x],result]

    return ''

def tieHigherCard(hand1,hand2):
    hand1 = sort(hand1)
    hand2 = sort(hand2)

    while len(hand1) > 0:
        value1 = cards.index( hand1[ len(hand1) - 1 ][0] )
        value2 = cards.index( hand2[ len(hand2) - 1 ][0] )

        if value1 > value2:
            return 0
        if value1 < value2:
            return 1
        
        hand1 = hand1[: len(hand1) - 1 ]
        hand2 = hand2[: len(hand2) - 1 ]

def compareHand(twoHands):
    global cards
    global winnerHands

    hand1 = twoHands[:5]
    hand2 = twoHands[5:]

    play1 = playInHand( hand1 )
    play2 = playInHand( hand2 )

    if play1 != '':
        print '\nPlayer 1:',printHand( hand1 ),'(',printPlay(play1),')'
    else:
        print '\nPlayer 1:',printHand( hand1 )
    if play2 != '':
        print 'Player 2:',printHand( hand2 ),'(',printPlay(play2),')'
    else:
        print 'Player 2:',printHand( hand2 )

    if len(play1) == 0 and len(play2) != 0:
        return 1
    if len(play1) != 0 and len(play2) == 0:
        return 0
    if len(play1) == 0 and len(play2) == 0:
        print 'Winning by highest card...'
        return tieHigherCard(hand1,hand2)
    
    
    value1 = winnerHands.index( play1[0] )
    value2 = winnerHands.index( play2[0] )

    if value1 > value2:
        return 0
    if value2 > value1:
        return 1
    
    print 'Tie with',winnerHands[value1]

    if value1 == 2:
        p1 = play1[1].split()
        p2 = play2[1].split()

        p1[0] = cards.index( p1[0] )
        p1[1] = cards.index( p1[1] )
        p2[0] = cards.index( p2[0] )
        p2[1] = cards.index( p2[1] )

        if p1[0] > p2[0]: return 0
        if p1[0] < p2[0]: return 1
        if p1[1] > p2[1]: return 0
        if p1[1] < p2[1]: return 1

        

    else:
        p1 = cards.index(play1[1])
        p2 = cards.index(play2[1])

        if p1 > p2: return 0
        if p1 < p2: return 1


    print 'Winning by highest card...'
    return tieHigherCard(hand1,hand2)


def main():
    counter = [0] * len(winnerHands)
    winnerCounter = [0,0]
    total = 0

    #with open( "p054_poker.txt" ) as f:
    with open( "p054_poker.txt" ) as f:
        for line in f:
            
            if '#' in line:
                print line
                continue

            total += 1

            separatedLine = line.split()

            winner = compareHand( separatedLine )

            if winner == 0:
                print bcolors.OKGREEN + 'Winner is player ' + str(winner+1) + bcolors.ENDC
            if winner == 1:
                print bcolors.OKBLUE + 'Winner is player ' + str(winner+1) + bcolors.ENDC

            winnerCounter[ winner ] += 1
    
    print '\n-----Statistics-----'
    print 'Total',total
    print 'Player 1 victories',winnerCounter[0],'(',100.0*winnerCounter[0]/total,'% )'
    print 'Player 2 victories',winnerCounter[1],'(',100.0*winnerCounter[1]/total,'% )'

main()