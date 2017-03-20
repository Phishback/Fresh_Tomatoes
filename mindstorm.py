import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
# Create brad object
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(5)
    for i in range(1, 36):
        draw_square(brad)
        brad.right(15)
        

    window.exitonclick()

draw_art()
