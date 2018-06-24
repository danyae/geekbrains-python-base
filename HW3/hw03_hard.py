# coding: utf-8
import os

__author__ = 'Ширгазин Даниил Олегович'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


class Fraction:
    def __init__(self, n=0, x=0, y=0):
        self.n = abs(n)
        self.x = abs(x)
        self.y = abs(y)
        self.sign = 1
        if n == 0 and x != 0:
            self.sign = abs(x) / x
        elif n != 0:
            self.sign = abs(n) / n
        self.__cut()  # Сокращаем дробь

    def __str__(self):
        if self.y == 0:
            return 'None'
        if self.n == 0 and self.x != 0:
            return "{0}{1}/{2}".format(self.__sign(), self.x, self.y)
        elif self.n == 0 and self.x == 0:
            return "0"
        elif self.n != 0 and self.x != 0:
            return "{0}{1} {2}/{3}".format(self.__sign(), self.n, self.x, self.y)
        elif self.n != 0 and self.x == 0:
            return "{0}{1}".format(self.__sign(), self.n)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.n == other.n and self.x == other.x and self.y == other.y and self.sign == other.sign
        else:
            return False

    def __cut(self):
        a = self.x
        b = self.y
        while b != 0:  # Ищем НОД
            temp = b
            b = a % b
            a = temp
        try:
            self.x = int(self.x / a)
            self.y = int(self.y / a)
            self.sign = int(self.sign)
        except ZeroDivisionError:
            return None

    def __sign(self):
        if self.sign < 0:
            return '-'
        else:
            return ''

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if other.y == 0 or self.y == 0:
                return None

            if other.y == self.y:
                new_n = 0
                new_x = (self.x * self.sign + self.n * self.y * self.sign) + \
                        (other.x * other.sign + other.n * other.y * other.sign)  # приводим целые части к знаменателю
                new_sign = 1
                if new_x != 0:
                    new_sign = abs(new_x) / new_x
                new_x = abs(new_x)
                while new_x - self.y > 0:  # Выделяем целую часть
                    new_x = new_x - self.y
                    new_n += 1
                return Fraction(new_n * int(new_sign), new_x, self.y)
            elif other.y != self.y:
                new_n = 0
                new_x = (self.x * self.sign + self.n * self.y * self.sign) * other.y + \
                        (other.x * other.sign + other.n * other.y * other.sign) * self.y
                new_y = self.y * other.y  # Не стал искать НОК, все равно потом сокращать
                new_sign = 1
                if new_x != 0:
                    new_sign = abs(new_x) / new_x
                new_x = abs(new_x)
                while new_x - new_y > 0:
                    new_x = new_x - new_y
                    new_n += 1
                return Fraction(new_n * int(new_sign), new_x, new_y)
        else:
            return None

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if other.y == 0 or self.y == 0:
                return None

            if other.y == self.y:
                new_n = 0
                new_x = (self.x * self.sign + self.n * self.y * self.sign) - \
                        (other.x * other.sign + other.n * other.y * other.sign)
                new_sign = 1
                if new_x != 0:
                    new_sign = abs(new_x) / new_x
                new_x = abs(new_x)
                while new_x - self.y > 0:
                    new_x = new_x - self.y
                    new_n += 1
                return Fraction(new_n * int(new_sign), new_x, self.y)
            elif other.y != self.y:
                new_n = 0
                new_x = (self.x * self.sign + self.n * self.y * self.sign) * other.y - \
                        (other.x * other.sign + other.n * other.y * other.sign) * self.y
                new_y = self.y * other.y
                new_sign = 1
                if new_x != 0:
                    new_sign = abs(new_x) / new_x
                new_x = abs(new_x)
                while new_x - new_y > 0:
                    new_x = new_x - new_y
                    new_n += 1
                return Fraction(new_n * int(new_sign), new_x, new_y)
        else:
            return None


def parse_input(s: str):
    action = ''
    if s.count(' - ') == 1:
        action = '-'
    elif s.count(' + ') == 1:
        action = '+'
    else:
        return None

    elements = s.split(' {} '.format(action))   # Делим строку на 2 дроби по действию
    fractions = []
    for el in elements:
        if len(el.split(' ')) > 1:  # Дробь с целой частью
            fraction_1_elems = el.split(' ')
            n = int(fraction_1_elems[0])
            x = int(fraction_1_elems[1].split('/')[0])
            y = int(fraction_1_elems[1].split('/')[1])
            fractions.append(Fraction(n, x, y))
        elif len(el.split(' ')) == 1:  # Дробь без целой части или целое число
            if len(el.split('/')) > 1:
                x = int(el.split('/')[0])
                y = int(el.split('/')[1])
                fractions.append(Fraction(0, x, y))
            elif len(el.split('/')) == 1:  # Целое число
                n = int(el)
                fractions.append(Fraction(n, 0, 1))

    if action == '-':
        return fractions[0] - fractions[1]
    if action == '+':
        return fractions[0] + fractions[1]
    return None

print('Задача 1')
a = Fraction(-1, 2, 4)
b = Fraction(1, 2, 4)
c = Fraction(2, 3, 4)
print('a = ', a)
print('b = ', b)
print('c = ', c)
print('Знак a:', a.sign)
print(b, '+', c, '=', b + c)
print(c, '+', c, '=', c + c)
print(c, '-', c, '=', c - c)
print(b, '-', c, '=', b - c)
print('5/6 + 4/7 =', parse_input('5/6 + 4/7'))
print('-2/3 - -2 =', parse_input('-2/3 - -2'))
print(Fraction(0, 0, 0))
print('c = c:', c == c)
print('a = c:', a == c)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

print('\nЗадача 2')
DIR = 'data'
workers = []
hours = []
with open(os.path.join(DIR, 'workers.txt'), 'r', encoding='UTF-8') as f:
    next(f)
    for line in f:
        values = line.split()
        worker = {'name': values[0], 'surname': values[1], 'salary': float(values[2]), 'job': values[3],
                  'hours_norm': float(values[4])}
        workers.append(worker)

with open(os.path.join(DIR, 'hours_of.txt'), 'r', encoding='UTF-8') as f:
    next(f)
    for line in f:
        values = line.split()
        worker = [x for x in workers if x['name'] == values[0] and x['surname'] == values[1]].pop()
        worker['hours_worked'] = float(values[2])

for worker in workers:
    if worker['hours_norm'] > worker['hours_worked']:
        factor = worker['hours_worked'] / worker['hours_norm']
        worker['next_salary'] = worker['salary'] * factor
    if worker['hours_norm'] < worker['hours_worked']:
        hour_norm = worker['salary'] / worker['hours_norm']
        worker['next_salary'] = worker['salary'] + (worker['hours_worked'] - worker['hours_norm']) * hour_norm
    if worker['hours_norm'] == worker['hours_worked']:
        worker['next_salary'] = worker['salary']
    print('{0} {1}: {2}'.format(worker['name'], worker['surname'], round(worker['next_salary'], 2)))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


print('\nЗадача 3')
DIR = 'data'
fruits = []
letters = list(map(chr, range(ord('А'), ord('Я')+1)))
with open(os.path.join(DIR, 'fruits.txt'), 'r', encoding='UTF-8') as f:
    for line in f:
        if line != '\n':
            fruits.append(line)

for letter in letters:
    fruits_on_letter = [x for x in fruits if x[0] == letter]
    if len(fruits_on_letter) > 0:
        with open(os.path.join(DIR, 'fruits_{0}.txt'.format(letter)), 'w', encoding='UTF-8') as f:
            f.writelines(fruits_on_letter)
