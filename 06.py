end = 100

sum_of_squares = 0
square_of_sums = 0

for x in range(1,end+1):
    sum_of_squares += x*x
    square_of_sums += x

square_of_sums *= square_of_sums

print str(square_of_sums) + " - " + str(sum_of_squares) + " = " + str(square_of_sums-sum_of_squares)