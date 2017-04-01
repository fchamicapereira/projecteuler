class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def readLine():
    text = []

    with open("p059_cipher.txt", "r") as f:
        for line in f:
            line.split()

            s = line.split(",")
            s[len(s) - 1] = s[ len(s) - 1].rstrip('\n')
            
            text += s

    return text


def expandPass( size, password ):
    passLen = len(password)
    newPass = ''

    if passLen == size:
        password
    
    lastCharIndex = password[ passLen - 1 ]
    counter = 0

    while len(newPass) != size:
        newPass += password[ counter % passLen ]
        counter += 1

    return newPass

def decipher( text, password ):
    newText = ''
    i = 0
    size = len(text)
    key = expandPass( len(text), password)

    while i < size:
        newText += str( unichr( int(text[i]) ^ ord(key[i]) ) )
        i += 1

    return newText

common = ['the','and','a','that']

line = readLine()

def contains( text, word ):
    word = word + ' '
    word2 = str(unichr(ord(word[0]) - 32)) + word[1:]

    if word in text or word2 in text:
        return True
    return False

def containsXTimes( text, word, times):
    word = word + ' '
    if text.count(word) >= times:
        return True
    return False

def dotRule(text):
    if text.count('.') == 0:
        return False
    
    size = len(text)
    indexes = [i for i, ltr in enumerate(text) if ltr == '.']

    for i in indexes:
        if i < size-1:
            if text[i+1] != ' ':
                return False

        if i < size - 3:
            c = ord( text[i+2] )
            if c < 65 or c > 90:
                return False

    return True

def highLightWords( text, common ):
    words = ''
    temp = ''

    for c in text:
        if ( ord(c) >= 65 and ord(c) <= 90) or ( ord(c) >= 97 and ord(c) <= 122):
            isWord = True
        else:
            isWord = False

            if temp != '':
                if temp in common:
                    words += bcolors.FAIL + temp + bcolors.ENDC
                else:
                    words += temp

            temp = ''
        
        if isWord:
            temp += c

        else:
            words += c

    print words

def sum(text):
    sum = 0
    for i in text:
        sum += ord(i)
    return sum

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            password = str(unichr(a)) + str(unichr(b)) + str(unichr(c))
            newText = decipher(line, password)
            
            condition = True
            for word in common:
                if contains(newText, word) == False:
                    if word != 'the':
                        print password,"doesn't give",word
                    condition = False
                    break
            
            if condition: 
                highLightWords( newText, common )
                print "password:",password
                print 'sum',sum(newText)
                exit(0)