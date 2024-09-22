import math


class Figure:
    def __init__(self):
        self.__sides = []
        self.__color = (0, 0, 0)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *new_sides):
        return (all(isinstance(x, int) and x > 0 for x in new_sides)
                and len(new_sides) == self.sides_count)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, circumference):
        super().__init__()
        self.__sides = [circumference]
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, a, b, c):
        super().__init__()
        self.set_sides(a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, side_length):
        super().__init__()
        self.set_sides(*(side_length for _ in range(12)))
        self.__side_length = side_length

    def get_volume(self):
        return self.__side_length ** 3


if __name__ == "__main__":
    circle = Circle(10)
    circle.set_color(255, 0, 0)
    print("Circle Color:", circle.get_color())
    print("Circle Area:", circle.get_square())

    triangle = Triangle(3, 4, 5)
    triangle.set_color(0, 255, 0)
    print("Triangle Color:", triangle.get_color())
    print("Triangle Area:", triangle.get_square())

    cube = Cube(3)
    cube.set_color(0, 0, 255)
    print("Cube Color:", cube.get_color())
    print("Cube Volume:", cube.get_volume())