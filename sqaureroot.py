def mysqrt(a):
    x = y
    y = (x + a/x) / 2
    print(y)
# print(mysqrt(1))

import math

def test_square_root(a):
    print(math.sqrt(a))
    x = y
    y = (x + a/x) / 2
    print(y)
    print(math.sqrt(a)-y)

print(test_square_root(1))



