import turtle

def koch_curve(t, length, level):
    """
    Рекурсивна функція для побудови кривої Коха.
    t — об'єкт turtle
    length — довжина лінії
    level — поточний рівень рекурсії
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def draw_snowflake(level):
    """
    Функція для побудови сніжинки Коха з трьох кривих
    """
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title(f"Koch Snowflake (Recursion level: {level})")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    for _ in range(3):
        koch_curve(t, 300, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    try:
        recursion_level = int(input("Enter recursion level (e.g., 0–5): "))
        if recursion_level < 0 or recursion_level > 6:
            print("⚠️ Please enter a level between 0 and 6 (too high = very slow!)")
        else:
            draw_snowflake(recursion_level)
    except ValueError:
        print("❌ Invalid input. Please enter an integer.")
