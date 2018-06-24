# coding: utf-8
import os

__author__ = 'Ширгазин Даниил Олегович'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print('Задача 1')
for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.mkdir(dir_path)
        print('Директория dir_{} создана'.format(i))
    except FileExistsError:
        print('Директория dir_{} уже существует'.format(i))

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
    try:
        os.rmdir(dir_path)
        print('Директория dir_{} удалена'.format(i))
    except FileNotFoundError:
        print('Директория dir_{} отсутствует'.format(i))

# В одну строку
# [os.mkdir(os.path.join(os.getcwd(), 'dir_{}'.format(x))) for x in range(1, 10)]
# [os.rmdir(os.path.join(os.getcwd(), 'dir_{}'.format(x))) for x in range(1, 10)]

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print('\nЗадача 2')
all_files = os.listdir(os.getcwd())
[print(x) for x in all_files if os.path.isdir(x)]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print('\nЗадача 3')
with open(__file__, 'r') as src, open(__file__ + '.dup', 'w') as dst:
    dst.write(src.read())

# или
# import shutil
# shutil.copy2(__file__, __file__ + '.dup1')
