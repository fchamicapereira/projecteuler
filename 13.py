lines = [line.rstrip('\n') for line in open('13.dat')]

digitsWanted = 10
counter = 0
carry = 0
sum = 0
totalDigits = len(lines[0])
result = ""
print("total digits = " + str(totalDigits))

while totalDigits > counter:
    sum = carry

    for line in lines:
        sum += int(line[totalDigits-1-counter])

    digit = (sum % 10)
    result = str(digit) + result

    carry = (sum - digit)/10
    counter += 1

    if totalDigits-1-counter < 0:
        result = str(carry) + result
        break

print result[:]
print len(result)
print result[:digitsWanted]