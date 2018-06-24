# coding: utf-8

__author__ = 'Ширгазин Даниил Олегович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    fib_list = [1, 1]
    for i in range(2, m):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[n-1:m]  # считаем что, ряд начинается с 1 элемента, а не с 0

print('Задача 1')
print(fibonacci(2, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sorted_list = list(origin_list)
    for i in reversed(range(len(origin_list))):
        for j in range(0, i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

print('\nЗадача 2')
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Решение не мое. Начал искать инфу, когда думал,
# как filter определяет, как вернуть коллекцию того же типа, как и пришла
# и понял что filter возвращает не коллекцию а итератор


def my_filter(func, seq):
    if func is None:
        return (x for x in seq if x)
    return (x for x in seq if func(x))

print('\nЗадача 3')
print(list(my_filter(lambda x: x > 0, range(-5, 5))))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        else:
            return False


def find_middle(p1: Point, p2: Point) -> Point:
    return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)


def check_parallelogram(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    m1 = find_middle(p1, p2)
    m2 = find_middle(p2, p3)
    m3 = find_middle(p3, p4)
    m4 = find_middle(p2, p4)
    m5 = find_middle(p1, p4)
    m6 = find_middle(p1, p3)
    middles = [m1, m2, m3, m4, m5, m6]
    for i in range(len(middles)):
        for j in range(i + 1, len(middles)):
            if middles[i] == middles[j] and i != j:
                return True
    return False

print('\nЗадача 4, вариант 1')
a1 = Point(0, 0)
a2 = Point(0, 2)
a3 = Point(3, 2)
a4 = Point(3, 0)
print(check_parallelogram(a1, a2, a3, a4))

# Понял, что можно было не выпендриваться
print('\nЗадача 4, вариант 2')
points = [(0, 0), (0, 2), (3, 2), (3, 0)]
middles = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        middles.append(((points[i][0] + points[j][0]) / 2, (points[i][1] + points[j][1]) / 2))

if len(middles) > len(set(middles)):
    print('Это параллелограмм')
else:
    print('Это не параллелограмм')
