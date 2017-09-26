import math

#result = 0

#for i in range(1000):
    #result = result + i + 1
    #print('in the {}th iteration, result = {}'.format(i, result))
    
#print(result)

result = 0

for i in range(0, 1001, 2):
    result = result + i

print(result)

for c in 'hello':
    print(c)

for alex in ['Hello', 'Chris', 'Stephanie']:
    print(alex)

import time
def countdown(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n = n - 1
    print('Blastoff!')

countdown(10)