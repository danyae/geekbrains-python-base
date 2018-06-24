# coding: utf-8
import os

__author__ = 'Ширгазин Даниил Олегович'


def create_folder_here(path):
    name = input('Введите название папки: ')
    dir_path = os.path.join(path, name)
    try:
        os.mkdir(dir_path)
        print('Успешно создано')
    except FileExistsError:
        print('Невозможно создать')


def remove_folder_here(path):
    name = input('Введите название папки: ')
    dir_path = os.path.join(path, name)
    try:
        os.rmdir(dir_path)
        print('Успешно удалено')
    except FileNotFoundError:
        print('Невозможно удалить')


def list_files(path):
    all_files = os.listdir(path)
    [print('DIR: ', x) for x in all_files if os.path.isdir(x)]
    [print('FILE: ', x) for x in all_files if not os.path.isdir(x)]


def go_to_folder(path):
    name = input('Введите название папки: ')
    temp = os.path.join(path, name)
    if os.path.exists(temp) and os.path.isdir(temp):
        print('Успешно перешел')
        return temp
    else:
        print('Невозможно перейти')
        return path
