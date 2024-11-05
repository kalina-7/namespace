class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled=True):
        self.sides = __sides
        self.color = __color
        self.filled = filled

    def get_color(self):
        return self.color

    def __is_valid_color(self, r, g, b):
        if r > 255 or g > 255 or b > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = [r, g, b]
        else:
            self.color = list(self.color)

    def __is_valid_sides(self, __sides):
        if __sides > 0 and self.__sides == __sides:
            return True
        else:
            return False

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)


    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.sides = list(new_sides)
        else:
            return


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *__sides):
        self.color = color
        self.sides = list(__sides)
        if len(self.sides) != Circle.sides_count:
            self.sides = [1]
        self.radius = self.sides[0]  / (2 * 3.14)


    def get_square(self):
        __radius = self.radius
        return __radius * __radius * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *__sides):
        self.color = color
        self.sides = list(__sides)
        if len(self.sides) != Triangle.sides_count:
            self.sides = [1, 1, 1]


    def get_square(self):
        p = sum(self.sides) / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *__sides):
        self.color = color
        self.sides = list(__sides)
        if len(self.sides) != 1:
            self.sides = [1] * Cube.sides_count
        else:
            self.sides = self.sides * Cube.sides_count


    def get_volume(self):
        return self.sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())