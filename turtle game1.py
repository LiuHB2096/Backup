from turtle import *
myTurtle = Turtle()

def writescore():
	name = screen.textinput("name box", "SCORE")
	myTurtle.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()