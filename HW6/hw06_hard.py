# coding: utf-8
import os
__author__ = 'Ширгазин Даниил Олегович'

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Worker:
    def __init__(self, line):
        values = line.split()
        self.name = values[0]
        self.surname = values[1]
        self.salary = float(values[2])
        self.job = values[3]
        self.hours_norm = float(values[4])
        self.hours_worked = 0
        self.next_salary = 0

DIR = 'data'
workers = {}
hours = []
with open(os.path.join(DIR, 'workers.txt'), 'r', encoding='UTF-8') as f:
    next(f)
    for line in f:
        worker = Worker(line)
        workers[worker.name + worker.surname] = worker

with open(os.path.join(DIR, 'hours_of.txt'), 'r', encoding='UTF-8') as f:
    next(f)
    for line in f:
        values = line.split()
        workers[values[0] + values[1]].hours_worked = float(values[2])

for worker in workers.values():
    if worker.hours_norm > worker.hours_worked:
        factor = worker.hours_worked / worker.hours_norm
        worker.next_salary = worker.salary * factor
    if worker.hours_norm < worker.hours_worked:
        hour_norm = worker.salary / worker.hours_norm
        worker.next_salary = worker.salary + (worker.hours_worked - worker.hours_norm) * hour_norm
    if worker.hours_norm == worker.hours_worked:
        worker.next_salary = worker.salary
    print('{0} {1}: {2:.2f}'.format(worker.name, worker.surname, worker.next_salary))
