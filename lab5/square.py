from turtle import Turtle, colormode
import turtle
import random
colormode(255)



#class Square(Turtle):
#	def __init__(self,size):
#		Turtle.__init__(self)
#		self.shapesize(size)
#		self.shape('square')

#	def random_color(self):
#		r= random.randint(0,256)
#		g= random.randint(0,256)
#		b= random.randint(0,256)
#		self.color(r,g,b)

#Kayvon = Square(10)
#Kayvon.random_color()
x=random.randint(-310,310)
y=random.randint(-265,265)

class Hexagon(Turtle):


	def __init__(self,size):
		Turtle.__init__(self)		
		self.ht()
		self.penup()
		self.begin_poly() 
		for i in range(6):
			
			self.fd(10)			
			self.left(360/6)
		self.end_poly()	
		turtle.register_shape('hexagon',self.get_poly())
		self.shape('hexagon')
		self.shapesize(size)
		self.goto(x,y)
		self.st()
	def random_color(self):
		r= random.randint(0,256)
		g= random.randint(0,256)
		b= random.randint(0,256)
		self.color(r,g,b)		

william= Hexagon(10)


turtle.mainloop()