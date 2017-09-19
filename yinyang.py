import turtle

franklin = turtle.Turtle()

print(franklin)

def yinyang(radius):
    franklin.pensize(10)
    franklin.circle(radius/2., 180)
    franklin.circle(radius, 180)
    franklin.left(180)
    franklin.circle(-radius/2., 180)
    franklin.left(90)
    franklin.up()
    franklin.forward(radius*0.35)
    franklin.right(90)
    franklin.down()
    franklin.circle(radius*0.15)
    franklin.left(90)
    franklin.up()
    franklin.backward(radius*0.35)
    franklin.down()
    franklin.left(90)
    

yinyang(200)
yinyang(200)

franklin.mainloop()
