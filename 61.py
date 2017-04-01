from functions import *

def cycle(number,l):
    size = len(l)
    i = 0
    result = []

    for r in l:
        if str(r)[:2] == str(number)[2:]:
            result.append(r)

    return result

def comb(s):
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

def main():
    digits = 4

    triangles   = generateNDigitsPolygonal(digits, triangle)
    squares     = generateNDigitsPolygonal(digits, square)
    pentagonals = generateNDigitsPolygonal(digits, pentagonal)
    hexagonals  = generateNDigitsPolygonal(digits, hexagonal) 
    heptagonals = generateNDigitsPolygonal(digits, heptagonal)
    octagonals  = generateNDigitsPolygonal(digits, octagonal)

    allPolygonals = [triangles,squares,pentagonals,hexagonals,heptagonals,octagonals]

    c = comb('012345')
    c.sort()

    for combination in c:
        n = map(int,list(combination))

        list1 = allPolygonals[ n[0] ]

        for t1 in list1:
            list2 = cycle( t1, allPolygonals[ n[1] ])

            if len( list2 ) == 0:
                continue

            for t2 in list2:
                list3 = cycle( t2, allPolygonals[ n[2] ])

                if len( list3 ) == 0:
                    continue

                for t3 in list3:
                    list4 = cycle( t3, allPolygonals[ n[3] ])

                    if len( list4 ) == 0:
                        continue

                    for t4 in list4:
                        list5 = cycle( t4, allPolygonals[ n[4] ])

                        if len( list5 ) == 0:
                            continue

                        for t5 in list5:
                            list6 = cycle( t5, allPolygonals[ n[5] ])


                            if len( list6 ) == 0:
                                continue

                            for t6 in list6:
                                allT = [t1,t2,t3,t4,t5,t6]
                                if cyclicList( allT ):
                                    print 'combination',combination
                                    print allT
                                    print 'sum',sum(allT)
                                    exit(1)
    
    

main()