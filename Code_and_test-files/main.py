import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        p = self.perimeter() / 2
        value = p * (p - self.a) * (p - self.b) * (p - self.c)
        return math.sqrt(max(value, 0))
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        x = abs(self.b - self.a)
        value = ((self.c + self.d) ** 2 - x ** 2) * (x ** 2 - (self.c - self.d) ** 2)
        if x == 0 or value < 0:
            return 0
        h = math.sqrt(value) / (2 * x)
        return ((self.a + self.b) / 2) * h
    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h
    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"

class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r ** 2
    def __str__(self):
        return f"Circle({self.r})"

def read_figures(filename):
    figures = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data = line.split()
            if not data:
                continue
            figure_type = data[0]
            params = list(map(float, data[1:]))

            if figure_type == "Triangle":
                a, b, c = params
                if a + b > c and a + c > b and b + c > a:
                    figures.append(Triangle(a, b, c))

            elif figure_type == "Rectangle":
                a, b = params
                if a > 0 and b > 0:
                    figures.append(Rectangle(a, b))

            elif figure_type == "Trapeze":
                a, b, c, d = params
                if a > 0 and b > 0 and c > 0 and d > 0:
                    figures.append(Trapeze(a, b, c, d))

            elif figure_type == "Parallelogram":
                a, b, h = params
                if a > 0 and b > 0 and h > 0:
                    figures.append(Parallelogram(a, b, h))

            elif figure_type == "Circle":
                r = params[0]
                if r > 0:
                    figures.append(Circle(r))

    return figures

files = ["input01.txt", "input02.txt", "input03.txt"]

for filename in files:
    figures = read_figures(filename)
    if not figures:
        print(f"\nФайл {filename}: немає коректних фігур")
        continue
    max_area = figures[0]
    max_perimeter = figures[0]
    for fig in figures:
        if fig.area() > max_area.area():
            max_area = fig
        if fig.perimeter() > max_perimeter.perimeter():
            max_perimeter = fig

    print(f"\nФайл: {filename}")
    print("Найбільша площа:")
    print(max_area, max_area.area())
    print("\nНайбільший периметр:")
    print(max_perimeter, max_perimeter.perimeter())
