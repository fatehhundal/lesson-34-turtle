import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.speed(3)

def draw_triangle():
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

def draw_rectangle():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

def draw_hexagon():
    t.penup()
    t.goto(200, 0)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    for _ in range(6):
        t.forward(70)
        t.left(60)
    t.end_fill()

draw_triangle()
draw_rectangle()
draw_hexagon()

t.hideturtle()
screen.mainloop()