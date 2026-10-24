import turtle
import random
import time
WIDTH = 500
HEIGHT = 500
COLORS = ['red', 'orange', 'green', 'yellow', 'blue', 'darkblue', 'purple', 'pink', 'black', 'grey']
def get_number_of_racers():
    while True:
        turtles = int(input("Введите колличество черепах от двух до десяти: "))
        if turtles < 2 or turtles > 10:
            print("Введите корректное значение")
            continue
        else:
            print("Отлично, начинаем гонку...")
            return turtles
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Стадион')
def create_turtles(colors):
    spacing = WIDTH // (len(colors) + 1)
    racers = []
    for number,color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.left(90)
        t.penup()
        t.setpos(-WIDTH // 2 + (number + 1) * spacing, -HEIGHT // 2 + 20)
        t.pendown()
        racers.append(t)
    return racers
def race(colors):
    turtles = create_turtles(colors)
    while True:
        for t in turtles:
            distance = random.randint(1, 20)
            t.forward(distance)
            x,y = t.pos()
            if y >= WIDTH//2 - 10:
                return colors[turtles.index(t)]
def main():
    random.shuffle(COLORS)
    colors = COLORS[:get_number_of_racers()]
    init_turtle()
    print(f"Победила черепаха {race(colors)} цвета!")
if __name__ == '__main__':
    main()