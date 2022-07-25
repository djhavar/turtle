import turtle

def form_sq(side):
    for i in range (4):
         my_pen.fd(side)
         my_pen.left(120)
         side -= 5

tut = turtle.Screen()
tut.bgcolor("white")
tut.title("turtle")

my_pen = turtle.Turtle()
my_pen.color("black")

tut = turtle.Screen()

side = 200

for i in range(10):
    form_sq(side)
    side -= 20