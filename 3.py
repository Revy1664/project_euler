from sympy import primerange, prod
from time import time

start = time()

####################################


primes = list(primerange(0, 100000))

for i in primes:
	if 600851475143 % i == 0:
		print(i)
		continue


####################################

end = time()

print(end - start)
