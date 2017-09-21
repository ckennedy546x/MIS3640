import time

def factor(n):
    if n == 1:
        return 1
    print('current n =', n)
    return n * factor(n-1)
    
print(factor(6))