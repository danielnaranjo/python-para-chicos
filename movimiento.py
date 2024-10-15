# reference: https://www.geeksforgeeks.org/turtle-programming-python/

# import 
import turtle

# declarate library
t = turtle.Pen()

def dibujo(forma="turtle", posicion=90) :
    # change logo
    t.shape(forma) # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”

def avanzar(pasos) :
    t.forward(pasos)

def retroceder(pasos) : 
    t.back(pasos)

def derecha(grados) :
    t.right(grados)

def izquierda(grados) :
    t.left(grados)

def mover(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def circulo(rad) :
    t.circle(rad)

def triangulo(side):
    for i in range(3):
        avanzar(side)
        izquierda(120)

def fin() :
    # prevent to close the screen
    t.getscreen()._root.mainloop()
    # Finish by turtle.done() command
    turtle.done()

# set movements
def comenzar() :
    # H
    mover(-400,50)
    avanzar(200)
    derecha(90)
    avanzar(90)
    derecha(90)
    avanzar(200)
    izquierda(90)
    avanzar(90)
    izquierda(90)
    avanzar(200)
    derecha(90)
    avanzar(90)
    derecha(90)
    avanzar(400)
    derecha(90)
    avanzar(90)
    derecha(90)
    avanzar(160)
    izquierda(90)
    avanzar(90)
    izquierda(90)
    avanzar(160)
    derecha(90)
    avanzar(90)
    derecha(90)
    avanzar(200)
    
    # O
    mover(150,-10)
    dibujo('circle')
    circulo(130)
    mover(130,-25)
    dibujo('square')
    circulo(80)

    # L 
    mover(170,-145)
    avanzar(200)
    derecha(90)
    avanzar(60)
    derecha(90)
    avanzar(150)
    izquierda(90)
    avanzar(60)
    derecha(90)
    avanzar(50)
    derecha(90)
    avanzar(120)

    # A
    mover(380,-15)
    dibujo('triangle')
    izquierda(60)
    triangulo(150)
    mover(350,-120)
    izquierda(120)
    triangulo(80)

    dibujo('turtle')
    mover(350,350)

def inicio(bgColor="white", title="Turtle") :
    tut = turtle.Screen()
    tut.bgcolor(bgColor)
    tut.title(title)
    t.setheading(90) # 90 center
    mover(0,100)
    dibujo()

inicio("green")
comenzar()
fin()


