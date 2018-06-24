# coding: utf-8

__author__ = 'Ширгазин Даниил Олегович'


def check_date(date: str) -> bool:
    """Проверка даты для задачи 2"""
    if len(date) != 10:
        return False
    if not (date[0].isdigit() and date[1].isdigit() and date[3].isdigit() and date[4].isdigit and date[6:9].isdigit()):
        return False
    if not(date[2] == '.' or date[5] == '.'):
        return False
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
    days_in_months = {'01': 31, '02': 30, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30,
                      '10': 31, '11': 30, '12': 31}
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_months[str(month)]:
        return False
    if year < 1 or year > 9999:
        return False
    return True


# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print('Задача 1')
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

expressions = equation.split(' ')
k = float(expressions[2].split('x')[0])
b = float(expressions[4])
y = k * x + b
print('y =', y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

print('\nЗадача 2')
dates = ['01.11.1985', '01.22.1001', '1.12.1001', '-2.10.3001']

for i in dates:
    print(i, '-', check_date(i)) 

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

print('\nЗадача 3')
n = int(input('Введите номер комнаты:\n'))
floor = 0
max_room_on_floor = 0  # комната с максимальным номером на этом этаже
floor_multiplier = 0  # умножатель текущего этажа: n этажей по n комнат
place_on_floor = 0  # позиция нашей комнаты слева

while max_room_on_floor < n:  # пока не доедем
    floor_multiplier += 1
    i = 1  # поднялись на позицию, после которой n этажей по n комнат, отсчитываем с 1 до n раз n комнат увеличивая i
    while i <= floor_multiplier:  # поднимаемся на лифте
        floor += 1  # приехали на следующий этаж
        max_room_on_floor += floor_multiplier
        i += 1
        if max_room_on_floor >= n:  # на этом этаже есть наша комната
            min_room_on_floor = max_room_on_floor - floor_multiplier + 1  # минимальный номер комнаты на этаже
            place_on_floor = n - min_room_on_floor + 1
            break  # приехали
print(floor, place_on_floor)
