import turtle

window = turtle.Screen()
window.bgcolor("red")

def  drawSquare():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(30)

    degrees = 360
    turn = 3
    while degrees > 0:
        sides = 4
        while sides > 0:
            brad.forward(200)
            brad.right(90)
            sides = sides - 1
        brad.right(turn)
        degrees = degrees - turn 

def drawCircle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def drawTriangle():
    chris = turtle.Turtle()
    chris.shape("triangle")
    chris.color("green")

    sides = 3
    while sides > 0:
        chris.forward(50)
        chris.left(120)
        sides = sides - 1

drawSquare()
#drawCircle()
#drawTriangle()
window.exitonclick()
