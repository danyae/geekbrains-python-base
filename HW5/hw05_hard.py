# coding: utf-8
import os
import sys
import shutil

__author__ = 'Ширгазин Даниил Олегович'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not argument:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), argument)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(argument))
    except FileExistsError:
        print('директория {} уже существует'.format(argument))


def ping():
    print("pong")


def current_dir():
    print(os.getcwd())


def copy_file():
    if not argument:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), argument)
    try:
        shutil.copy2(file_path, file_path + '.copy')
    except FileNotFoundError:
        print('Файл не найден')


def remove_file():
    if not argument:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), argument)
    try:
        if input("Удалить файл {}? (Y) ".format(argument)) == 'Y':
            os.remove(file_path)
        else:
            print("Файл не был удален")
    except FileNotFoundError:
        print('Файл не найден')

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "ls": current_dir
}

try:
    argument = sys.argv[2]
except IndexError:
    argument = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
