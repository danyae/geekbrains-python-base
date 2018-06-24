# coding: utf-8
import random
__author__ = 'Ширгазин Даниил Олегович'

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Cell:
    def __init__(self, num: int):
        self.number = num
        self.crossed_out = False

    def __repr__(self):
        if self.number < 1:  # Пустые клетки
            return '   '
        if self.crossed_out:
            return ' --'
        else:
            return '{:>3}'.format(self.number)


class Card:
    def __init__(self, name):
        self.name = name
        self.cells = []
        self.nums_dict = {}  # Числа и их позиция на карточке 1: (0, 5)
        self.fill_cells()

    def fill_cells(self):
        numbers = random.sample(range(1, 91), 15)
        for row in range(0, 3):
            line = []
            nums_current_line = sorted(numbers[0:5])  # 5 чисел для строки карточки
            del numbers[0:5]
            for col in range(0, 5):
                line.append(Cell(nums_current_line[col]))
            for val in range(0, 4):  # 4 рандомных пустых места для строки карточки
                index = random.randint(0, len(line))
                line.insert(index, Cell(0))
            self.cells.append(line)
            for col in range(0, 9):  # Сформировали строку, пройдемся еще раз и запишем в словарь, что где лежит
                if line[col].number != 0:
                    self.nums_dict[line[col].number] = (row, col)

    def cross_cell(self, num):
        if num in self.nums_dict:
            coord = self.nums_dict[num]
            self.cells[coord[0]][coord[1]].crossed_out = True
            del self.nums_dict[num]
            return True
        return False

    def card_won(self):
        return True if len(self.nums_dict) == 0 else False

    def __str__(self):
        line = ''
        line += '{:-^27}\n'.format(self.name)
        for row in self.cells:
            for cell in row:
                line += str(cell)
            line += '\n'
        line += '-' * 27
        return line


class Bag(object):
    def __init__(self):
        self.numbers = list(range(1, 91))

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.numbers) == 0:
            raise StopIteration
        num = random.choice(self.numbers)
        self.numbers.remove(num)
        return num

    def __len__(self):
        return len(self.numbers)


def check_winner(*args):
    won_condition = False
    for card in args:
        if card.card_won():
            print('*' * 50)
            print('{:*^50}'.format('  {0} - победила!  '.format(card.name)))
            print('*' * 50)
            won_condition = True
    return won_condition


def do_move(card, num, cross_out: bool):
    condition = card.cross_cell(num)
    if condition == cross_out:  # Хотел зачеркнуть и удалось или не хотел зачеркнуть и правильно сделал
        return True
    else:
        print('*' * 50)
        print('{:*^50}'.format('  {0} - проиграла!  '.format(card.name)))
        print('*' * 50)
        return False

my_card = Card('Ваша карточка')
ai_card = Card('Карточка компьютера')
bag = Bag()

for number in bag:
    print('Новый бочонок: {0} (осталось {1})'.format(number, len(bag)))
    print(my_card)
    print(ai_card)
    ai_card.cross_cell(number)
    move = ''
    while move != 'y' and move != 'n' and move != 'q':
        move = input('Зачеркнуть цифру? (y/n/q)\n')
    if move == 'y':
        if not do_move(my_card, number, True):
            break
    if move == 'n':
        if not do_move(my_card, number, False):
            break
    if move == 'q':
        print('Игра окончена')
        break
    if check_winner(my_card, ai_card):
        break

