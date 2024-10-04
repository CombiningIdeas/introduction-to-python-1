import turtle

def move(a):
    turtle.forward(a)
    turtle.left(90)

def drawSquare(a):
    for i in range(4):
        move(a)

def drawSquareColor(a, color):
    turtle.color(color)
    turtle.begin_fill()
    drawSquare(a)
    turtle.end_fill()

    
turtle.speed(2)

drawSquareColor(60, "red")
turtle.goto(150, 50)
drawSquareColor(90, "green")


turtle.goto(-250, -200)
drawSquareColor(60, "blue")
turtle.goto(-300, -150)
drawSquareColor(100, "violet")


turtle.goto(200, 300)
drawSquareColor(70, "Orange")
turtle.goto(150, 150)
drawSquareColor(130, "black")


turtle.goto(-350, -100)
drawSquareColor(150, "gray")
turtle.goto(-150, -55)
drawSquareColor(90, "yellow")

