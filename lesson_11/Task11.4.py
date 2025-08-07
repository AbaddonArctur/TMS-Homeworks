from math import pi
from math import sqrt

class Sphere:
    def __init__(self, rad=1, x=0, y=0, z=0):
        self.rad = rad
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4 * pi * self.rad ** 3) / 3

    def get_square(self):
        return 4 * pi * self.rad ** 2

    def get_radius(self):
        return self.rad

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, rad):
        self.rad = rad

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        d = sqrt(((x - self.x) ** 2) + ((y - self.y) ** 2) + ((z - self.z) ** 2))
        return d <= self.rad

figure = Sphere(5, 3, 4, -2)

print(f"Объём шара: {figure.get_volume()}")
print(f"Площадь шара: {figure.get_square()}")
print(f"Радиус шара: {figure.get_radius()}")
print(f"Центр шара: {figure.get_center()}")
print("Устанавливаем новый радиус шара")
figure.set_radius(7)
print("Устанавливаем новый центр шара")
figure.set_center(0, 0, 0)
print(f"Радиус шара: {figure.get_radius()}")
print(f"Центр шара: {figure.get_center()}")
print(f"Точка внутри шара: {figure.is_point_inside(3, 6, 4)}")