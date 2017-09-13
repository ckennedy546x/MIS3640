print(60*42+42) #Beginning of Exercise for Session 1
print(10/1.61)
print(6.21/2562)
print(.00242388*60)
print(.1454327*60)

print((4/3)*3.1415926*5*5*5) #Beginning of Exercise for Session 2 #1 
print((24.95*.6*60)+(59*.75)+3)#2
print(((8*60+15)*2)+((7*60+12)*3))#3
print(2286/60)
print('7:30:06AM')#Home arrival time
print((89-82)/82*100)
print('Percentage of grade increase is: %02.0d %%' % 8.5365)

#Beginning of Exercise for Session 3
import time
date = time.time()
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date)))

import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60) // 60 % 24

#Class Session 4 Exercises

def my_abs(x):
    print(abs(x))

my_abs(-400)

def give_me_a_break():
    str1 = 'break'
    return str1
    print('another break')

print(give_me_a_break())

def nop():
    pass


import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
#Exercise 1
import math
def quadratic(a, b, c, x):
    y = ((a*x)**2)+(b*x)+c
    return y
ans = quadratic(2, 4, 8, 2/3)
print(ans)
