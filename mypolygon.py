# Exercise 1

import turtle

franklin = turtle.Turtle()

print(franklin)

# for i in range(4):
    # franklin.fd(100)
    # franklin.lt(90)





# turtle.mainloop()

# Exercise 2

import turtle

franklin = turtle.Turtle()

print(franklin)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
# polygon(franklin, 200, 8)


import math

# def circle(t, r):
 # circumf = 2 * math.pi * r
    # n = 50
    # length = circumf / n
    # polygon(t, length, n)

# circle(franklin, 8)

def arc(t, r, angle):
     arc_length = 2 * math.pi * r * angle / 360
     n = int(arc_length / 3) + 1
     step_length = arc_length / n
     step_angle = angle / n
     for i in range(n):
         t.fd(step_length)
         t.lt(step_angle)

# arc(franklin, 100, 180)

# turtle.mainloop()

def 
    