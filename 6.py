from time import time


start = time()

###################################

sum_of_squares = sum([x**2 for x in range(101)])
square_of_sum = sum([x for x in range(101)])**2

print(square_of_sum - sum_of_squares)

###################################

end = time()

print(end - start)
