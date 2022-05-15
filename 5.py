from time import time
from math import lcm

start = time()

###################################

print(lcm(*list(range(1, 20))))

###################################

end = time()

print(end - start)
