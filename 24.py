def insert(x,c):
    result = []
    for i in range(0,len(x)+1):
        result.append(x[:i] + c + x[i:])
    return result

def permutation(s):
    result = [s[0]]
    temp = []
    for c in s:
        if c == s[0]:
            continue
        for string in result:
            temp.extend(insert(string,c))
        result = temp
        temp = []
    result.sort()
    return result

s = '0123456789'
print permutation(s)[999999]
            
        
        
