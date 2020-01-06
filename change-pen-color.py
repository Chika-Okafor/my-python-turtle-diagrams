import turtle 

painter = turtle.Turtle()

painter.pencolor("#f85de") #You can use HEX code for the colors
for i in range(24):
    painter.forward(i*10)
    painter.left(90)
        
painter.pencolor("red")
for i in range(40):
    painter.forward(100)
    painter.left(123)
    
painter.pencolor("green")
for i in range(50):
    painter.forward(i*5)
    painter.right(123)
    
turtle.done()