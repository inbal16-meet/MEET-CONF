import turtle
turtle.speed(9)
#making the board
def draw_board(q,w):
	turtle.penup()
	turtle.goto(q-200,w-200)
	turtle.pendown()
	turtle.goto(q+400,w-200)
	turtle.goto(q+400,w+400)
	turtle.goto(q-200,w+400)
	turtle.goto(q-200,w-200)


#know where mouse is
x,y=turtle.position()


#stamp 1
def stamp1(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.circle(20)
	turtle.circle(40)


turtle.shape("turtle")
	

#stamp 2
def stamp2(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x,y+20)
	turtle.goto(x+20,y)
	turtle.goto(x-20,y)
	turtle.goto(x,y+20)


#when clicked, post stamp.
turtle.onscreenclick(stamp2, btn=1 , add= True)
turtle.onscreenclick(stamp1, btn =3  ,add=True)
#clear
def clear():
	turtle.clear()
#COLOR CHANGING
def Switch_color1():
	turtle.color("red")

def Switch_color2():
	turtle.color("blue")
#when pressing O, change color

turtle.getscreen().onkeypress(Switch_color2,"o")
#press p = change color 
turtle.getscreen().onkeypress(Switch_color1, "p")
#clear
turtle.getscreen().onkeypress(clear, "c")



#dragging left click

turtle.ondrag(stamp1, btn=1, add=True)

#dragging right click

turtle.ondrag(stamp2, btn=2, add=True)


turtle.getscreen().listen()
turtle.mainloop()
