import random
from turtle import Turtle, Screen
Race = False

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Escoge tu equipo", prompt="Selecciona el color (red,orange,yellow,blue,violet): ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]

turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=-100 + 50 * i)
    turtles.append(t)

if bet:
    Race = True

while Race:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            Race = False
            winning = turtle.pencolor()
            
            if winning == bet:
                print("Eres el ganador! La tortuga "+ winning +" ganó!!!")
                turtle.write("Eres el ganador! La tortuga "+ winning +" ganó!!!")
            else:
                print("Perdiste :( Ganó la tortuga "+ winning +"...")
                turtle.write("Perdiste :( Ganó la tortuga "+ winning +"...")

        distance = random.randint(0, 10)
        turtle.forward(distance)

s.exitonclick()