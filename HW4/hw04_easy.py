# coding: utf-8
import random

__author__ = 'Ширгазин Даниил Олегович'

# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print('Задача 1')
numbers = [random.randint(0, 100) for _ in range(10)]
numbers_pow = [x ** 2 for x in numbers]
for num, num_pow in zip(numbers, numbers_pow):
    print('x: {0:>2}, x^2: {1:>4}'.format(num, num_pow))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('\nЗадача 2')
fruits_1 = ['яблоко', 'банан', 'апельсин', 'груша', 'абрикос', 'ананас', 'лимон']
fruits_2 = ['виноград', 'банан', 'апельсин', 'дыня', 'инжир', 'лимон']
fruits_common = [el for el in fruits_1 if el in fruits_2]
print(fruits_common)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print('\nЗадача 3')
numbers = [random.randint(-100, 100) for _ in range(100)]
# Стоит включать несколько условий в скобки, чтобы лучше читалось?
numbers_filter = [x for x in numbers if (x % 3 is 0) and (x > 0) and (x % 4 is not 0)]
print(numbers_filter)
