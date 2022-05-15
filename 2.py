import time

start = time.time()


#########################################

fb1 = fb2 = 1

summ = 0

while True:
	fb1, fb2 = fb1+fb2, fb1
	if fb1 % 2 == 0:
		summ += fb1
	elif fb1 > 4000000:
		break

print(summ)

########################################


end = time.time()

print(end - start)
