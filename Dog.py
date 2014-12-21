import turtle
turtle1= turtle.Turtle()
turtle2= turtle.Turtle()
loop()
	if (x1=x2):
		print("game over!")
	else
		turtle1.goto(x1,y1+5)
		turtle2.goto(x2,y2+5)

#turtle 2
def turn_left2():
	turtle1.rotate(180)


def turn_right2():
	turtle1.rotate(90)


#for turtle1

def turn_left1():
	turtle1.rotate(180)


def turn_right1():
	turtle1.rotate(90)


turtle.getscreen().onkeypress(turn_right, "right")


turtle.getscreen().onkeypress(turn_left, "left")



turtle.getscreen().listen()
turtle.mainloop
