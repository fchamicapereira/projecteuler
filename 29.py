def distinctPowers(start,end):
    results = []

    for a in range(start,end+1):
        for b in range(start,end+1):
            n = pow(a,b)
            if n not in results:
                results.append(n)

    results.sort()
    return results

print len(distinctPowers(2,100))