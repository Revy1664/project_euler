from time import time


start = time()

###################################

numbers = set((x*y) for x in xrange(1, 999) for y in xrange(1, 999) if str(x*y) == str(x*y)[::-1])

print(max(numbers))

###################################

end = time()

print(end - start)
