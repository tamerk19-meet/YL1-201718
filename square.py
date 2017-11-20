from turtle import Turtle, colormode
import turtle
import random
colormode(255)



class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape('square')

	def random_color(self):
		r= random.randint(0,256)
		g= random.randint(0,256)
		b= random.randint(0,256)
		self.color(r,g,b)

Kayvon = Square(10)
Kayvon.random_color()
turtle.mainloop()