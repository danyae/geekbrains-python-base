# coding: utf-8

__author__ = 'Ширгазин Даниил Олегович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):
    if ndigits < 0:
        return None
    ndigits_pow = 10 ** ndigits  # Передвинем запятую на ndigits знаков вправо и отбросим дробную часть
    number_pow_int = number * ndigits_pow // 1
    number_round_left = number_pow_int / ndigits_pow  # Подготовим 2 числа, с округлением влево и вправо
    number_round_right = (number_pow_int + 1) / ndigits_pow
    difference = 5 / (ndigits_pow * 10)  # Сравним их разность с исходным числом
    if number_round_right - number > difference:
        return number_round_left
    else:
        return number_round_right

print('Задача 1')
print(my_round(2.1234567, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    numbers = list(str(ticket_number))  # Без разницы, что на входе: строка или число
    numbers = list(map(int, numbers))
    if sum(numbers[0:3]) == sum(numbers[3:6]):
        return True
    else:
        return False

print('\nЗадача 2')
print(lucky_ticket(111111))
print(lucky_ticket('222111'))

