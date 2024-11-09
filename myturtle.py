import turtle

#set up the screen
screen = turtle.Screen()

screen.bgcolor("#a3e37e")

#Create a turtle instance
my_turtle = turtle.Turtle()

#Change the appearance and speed of the turtle
my_turtle.color("#ff5a0e")
my_turtle.shape("turtle")
my_turtle.speed(20)

def movePen(x , y):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()

#Move the turtle to the starting point of the body

#Body
movePen(0, -100)
my_turtle.circle(100)

#Head
movePen(0, 100)
my_turtle.circle(40)

#Left Hand
movePen(-104, 40)
my_turtle.circle(20)

#Right Hand
movePen(104, 40)
my_turtle.circle(20)

#Left Foot
movePen(-80, -98)
my_turtle.circle(15)

#Right Foot
movePen(80, -98)
my_turtle.circle(15)

def drawline(x1, y1, x2, y2):
    my_turtle.penup()
    my_turtle.goto(x1, y1)
    my_turtle.pendown()
    my_turtle.goto(x2, y2)

#Tail
drawline(10,-100, 0,-120)
drawline(0, -120, -10 ,-100)

turtle.done()