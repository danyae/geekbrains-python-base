# coding: utf-8
import math

__author__ = 'Ширгазин Даниил Олегович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


class Side:
    @staticmethod
    def side(x, y):
        return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


class Triangle(Side):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self.ab = self.side(a, b)
        self.bc = self.side(b, c)
        self.ca = self.side(c, a)
    
    def perimeter(self):
        return self.ab + self.bc + self.ca

    def height(self, side):
        return self.area() * 2 / side

    def area(self):
        halfperim = self.perimeter() / 2
        return math.sqrt(halfperim * (halfperim - self.ab) * (halfperim - self.bc) * (halfperim - self.ca))

print('\nЗадача 1')
triang = Triangle((0, 0), (0, 2), (1, 0))
print('Side (0,0), (0,2):', Triangle.side((0, 0), (0, 2)))
print('Perimeter: ', triang.perimeter())
print('AB:', triang.ab)
print('BC:', triang.bc)
print('CA:', triang.ca)
print('Area:', triang.area())
print('Height AB: ', triang.height(triang.ab))
print('Height BC: ', triang.height(triang.bc))
print('Height CA: ', triang.height(triang.ca))


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid(Side):
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self.ab = self.side(a, b)
        self.bc = self.side(b, c)
        self.cd = self.side(c, d)
        self.da = self.side(d, a)

    def istrapezoid(self):
        k1 = (self._d[1] - self._a[1]) / (self._d[0] - self._a[0])
        k2 = (self._c[1] - self._b[1]) / (self._c[0] - self._b[0])
        k3 = (self._b[1] - self._a[1]) / (self._b[0] - self._a[0])
        k4 = (self._d[1] - self._c[1]) / (self._d[0] - self._c[0])
        return k1 == k2 or k3 == k4

    def isorthogonal(self):
        if self.istrapezoid():
            return self.side(self._a, self._c) == self.side(self._b, self._d)
        return False

    def area(self):
        if not self.isorthogonal():
            return None
        # Для формулы площади по стороным найдем бедро c
        # и основания a и b, где a > b
        a = None
        b = None
        if self.ab == self.cd:
            c = self.ab
            if self.da > self.bc:
                a = self.da
                b = self.bc
            else:
                a = self.bc
                b = self.da
        else:
            с = self.bc
            if self.ab > self.cd:
                a = self.ab
                b = self.cd
            else:
                a = self.cd
                b = self.da
        return (a + b) / 4 * math.sqrt(4 * (c ** 2) - (a - b) ** 2)

    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da


print('\nЗадача 2')
trapezoid = Trapezoid((0, 0), (1, 2), (5, 2), (6, 0))
print('Это трапеция: ', trapezoid.istrapezoid())
print('Это равнобокая трапеция: ', trapezoid.isorthogonal())
print('Периметр: ', trapezoid.perimeter())
print('Стороны: ab - {0:.2f}, bc - {1:.2f}, cd - {2:.2f}, da - {3:.2f}'.format(trapezoid.ab, trapezoid.bc,
                                                                               trapezoid.cd, trapezoid.da))
print('Площадь трапеции: {0:.3f}'.format(trapezoid.area()))
