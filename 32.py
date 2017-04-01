def pandigital(x,n):
    l = map(int,str(x))

    for x in range(1,n+1):
        if l.count(x) != 1:
            return False
    return True

def repeatDigits(x):
    l = map(int,str(x))

    for d in l:
        if l.count(d) > 1:
            return True
    
    return False

def nDigits(n):
    s = list(str(n))
    return len(s)

def intWithCommas(x):
    if type(x) not in [type(0), type(0L)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

limitD = 9
products=[]
finish = pow(10,limitD-1)-1
limitDigitsMultiplicand = int(limitD/2)+1

for digitsMultiplicand in range(1,limitDigitsMultiplicand):
    start   = pow(10,digitsMultiplicand-1)
    end     = pow(10,digitsMultiplicand)

    print "new cycle " + intWithCommas(start) + " --> " + intWithCommas(end)

    for multiplicand in range(start,end):

        if repeatDigits(multiplicand):
            continue

        for multiplier in range(1,multiplicand):
            product = multiplicand*multiplier
            result = int(str(multiplicand) + str(multiplier) + str(product))

            if nDigits(result) > 9:
                break

            if repeatDigits(multiplier):
                continue

            if pandigital(result,9) and product not in products:
                products.append(product)
                print str(multiplicand) + " * " + str(multiplier) + " = " + str(product)

print products

sum = 0
for x in products:
    sum += x

print sum