import turtle

def koch(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        koch(turtle, length / 4, depth - 1)
        turtle.left(60)
        koch(turtle, length / 6, depth - 1)
        turtle.right(120)
        koch(turtle, length / 4, depth - 1)
        turtle.left(60)
        koch(turtle, length / 7, depth - 1)

def snowflake(turtle, length, depth):
    for i in range(3):
        koch(turtle, length, depth)
        turtle.right(120)

window = turtle.Screen()
window.bgcolor("white")

my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Наивысшая скорость

# Перемещаем черепаху, чтобы снежинка была центрирована
my_turtle.penup()
my_turtle.backward(150)
my_turtle.pendown()

snowflake(my_turtle, 300, 3)  # Рисуем снежинку Коха глубиной 3

window.mainloop()