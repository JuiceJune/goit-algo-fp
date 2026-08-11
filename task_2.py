import math
import turtle


def pythagoras_tree(t, size, level):
    if level == 0:
        return

    t.forward(size) # малюємо стовбур/гілку

    branch_size = size / math.sqrt(2)

    t.left(45)
    pythagoras_tree(t, branch_size, level - 1) # лівк піддерево
    t.right(90)
    pythagoras_tree(t, branch_size, level - 1) # праве піддерево
    t.left(45) # повертаємо heading до того, що було після t.forward(size)

    t.backward(size) # повертаємось у вихідну точку цього викликy


def main():
    level = int(input("Введіть рівень рекурсії дерева: "))

    screen = turtle.Screen()
    screen.tracer(0) # малюємо все і показуємо одним разом

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.setposition(0, -200)
    t.setheading(90) # ростимо вгору
    t.pendown()

    pythagoras_tree(t, 100, level)

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
