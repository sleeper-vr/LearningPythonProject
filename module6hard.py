import math


class Figure():
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        if len(sides) != self.sides_count:
            sides = [1] * self.sides_count
        self.set_sides(*sides)
        self.set_color(*color)
        self.filled = filled

    def __is_valid_color(self, color):
        return all(0 <= i <= 255 for i in color)

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        return len(sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(0,0,0), side=0, filled=False):
        super().__init__(color, side, filled=filled)
        self.set_radius()

    def set_radius(self):
        self.__radius = self.get_sides()[0] / math.pi / 2

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.set_radius()

    def get_square(self):
        return round(math.pi * self.__radius ** 2, 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0,0,0), side=0, filled=False):
        sides = [side] * 12
        super().__init__(color, *sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((100, 150, 200), 10, 20, 30)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
triangle1.set_color(100, 150, -20) # Не изменится
print(triangle1.get_color())
triangle1.set_color(50, 50, 150) # Изменится
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
triangle1.set_sides(15, 25, 25) # Изменится
print(triangle1.get_sides())
triangle1.set_sides(15, 25) # Не изменится
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка периметра (треугольника):
print(len(triangle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка площади (треугольника):
print(triangle1.get_square())

# Проверка площади (круга):
print(circle1.get_square())

