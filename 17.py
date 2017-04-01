numbers1 =  ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
numbers2 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
numbers3 = ['','hundred','thousand','million','billion']

def orderOne(x):
    return numbers1[x]

def orderTwo(x):
    if x < 20:
        return numbers1[x]

    secondDigit = x % 10
    firstDigit = (x - secondDigit) / 10

    if x % 10 == 0:
        return numbers2[firstDigit]

    return numbers2[firstDigit] + "-" + numbers1[secondDigit]

def orderThree(x):
    digit = int(x/100)
    otherDigits = x - digit*100

    if otherDigits == 0:
        return numbers1[digit] + " " + numbers3[1]

    return numbers1[digit] + " " + numbers3[1] + " and " + orderTwo(otherDigits)

def orderFourToSix(x):
    firstThreeDigits = int(x / 1000)
    otherDigits = x - firstThreeDigits * 1000

    if otherDigits == 0:
        return text( firstThreeDigits ) + " " + numbers3[2]

    if int(otherDigits / 100) != 0:
        return text( firstThreeDigits ) + " " + numbers3[2] + ", " + text (otherDigits)
    else:
        return text( firstThreeDigits ) + " " + numbers3[2] + " and " + text (otherDigits)

def text(x):
    nDigits = len(str(x))

    if nDigits == 1:
        return orderOne(x)
    if nDigits == 2:
        return orderTwo(x)
    if nDigits == 3:
        return orderThree(x)
    if nDigits > 3 and nDigits < 7:
        return orderFourToSix(x)

def count_letters(word):
    BAD_LETTERS = " ,-"
    return len([letter for letter in word if letter not in BAD_LETTERS])

sum = 0
for x in range(1,1001):
    sum += count_letters(text(x))
print sum