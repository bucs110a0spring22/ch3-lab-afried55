import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for x in range(1,11):
  michelangelo.forward(random.randrange(1,11))
  leonardo.forward(random.randrange(1,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
# Part B - complete part B here
leonardo.down()
shape_sides = (3,4,6,9,12)
for side in shape_sides:
  angle = 360/side
  side_range = side+1
  for i in range(1,side_range):
    leonardo.left(angle)
    leonardo.forward(100)
  leonardo.clear()  


window.exitonclick()
