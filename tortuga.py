# import
import turtle

# declarate library
t = turtle.Pen()

# change logo
t.shape("turtle") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
t.setheading(90)

# set movements
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.right(60) 
t.forward(100) 
t.right(60) 
t.forward(100) 
t.right(60) 
t.forward(100) 
t.right(60) 
t.forward(100) 
t.right(60) 
t.forward(100)

# prevent to close the screen
t.getscreen()._root.mainloop()

# Finish by turtle.done() command
turtle.done()