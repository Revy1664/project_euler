from time import time
from sympy import primerange

start = time()

###################################


i = 10000

while True:
	if len(tuple(primerange(i))) >= 10001:
		numbers = tuple(primerange(i))
		break

	i += 100000

print(numbers[:10001][-1])

###################################

end = time()

print(end - start)
