import turtle
import math

def draw_pythagoras_tree(branch_length, level):
    """Функція для малювання дерева Піфагора"""
    if level == 0:
        return

    # Малюємо гілку
    turtle.forward(branch_length)

    #Save the current position and angle
    position = turtle.position()
    heading = turtle.heading()

    #left branch
    turtle.left(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    #Restore the position and angle
    turtle.setposition(position)
    turtle.setheading(heading)

    #Right branch
    turtle.right(45)
    draw_pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)

    #Restore the position and angle
    turtle.setposition(position)
    turtle.setheading(heading)

    def main():
        turtle.speed("fastest")
        turtle.left(90)  # Повертаємо черепаху вгору
        turtle.up()
        turtle.goto(0, -200)  # Початкова позиція
        turtle.down()
        turtle.color("green")

level = int(input("Введіть рівень дерева (наприклад, 5-10): "))
draw_pythagoras_tree(100,level)

turtle.done()

if __name__ == "__main__":
    main()


    
