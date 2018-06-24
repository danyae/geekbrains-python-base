# coding: utf-8

__author__ = 'Ширгазин Даниил Олегович'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School:
    def __init__(self, school_name, school_adress, teachers:list, students:list, courses:dict, classrooms:list):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers  # список объектов Teacher
        self._students = students  # список объектов Student
        self._courses = courses
        self._classrooms = classrooms

    def get_classrooms(self):
        return [x.class_name for x in self._classrooms]

    def get_students_in_class(self, class_room):
        return [x.short_name for x in self._students if x.class_room_name == class_room]

    def get_courses_for_student(self, student):
        class_room = [x for x in self._classrooms if x.class_name == student.class_room_name][0]
        return [self._courses[x] for x in class_room.course_keys]

    def get_teachers_in_class_room(self, class_room_name):
        return [x for x in self._teachers if class_room_name in x.classes]


class ClassRoom:
    def __init__(self, name, course_keys):
        self._name = name
        self._course_keys = course_keys

    @property
    def class_name(self):
        return self._name

    @property
    def course_keys(self):
        return self._course_keys


class Person:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name


class Student(Person):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mother, father):
        Person.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mother': mother,
            'father': father,
            }

    @property
    def short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name, self._first_name[0], self._middle_name[0])

    @property
    def class_room_name(self):
        return self._class_room

    @property
    def parents(self):
        return self._parents


class Teacher(Person):
    def __init__(self, last_name, first_name, middle_name, course_keys, classes):
        Person.__init__(self, last_name, first_name, middle_name)
        self._course_keys = course_keys
        self._classes = classes

    @property
    def course_keys(self):
        return self._course_keys

    @property
    def classes(self):
        return self._classes

    def __str__(self):
        return '{0} {1}.{2}.'.format(self._last_name, self._first_name[0], self._middle_name[0])

courses = {0: 'математика', 1: 'русский язык', 2: 'физика', 3: 'география', 4: 'химия'}

classroom_1 = ClassRoom('5А', [0, 1, 2])
classroom_2 = ClassRoom('5Б', [0, 1, 2])
classroom_3 = ClassRoom('6А', [0, 1, 2, 3])
classroom_4 = ClassRoom('7А', [0, 1, 2, 3, 4])
classrooms = [classroom_1, classroom_2, classroom_3, classroom_4]

teacher_1 = Teacher('Иванова', 'Мария', 'Ивановна', [0], ['5А', '5Б', '6А', '7А'])
teacher_2 = Teacher('Петрова', 'Татьяна', 'Петровна', [1], ['5А', '5Б', '6А', '7А'])
teacher_3 = Teacher('Сидорова', 'Анна', 'Сидоровна', [2], ['6А', '7А'])
teacher_4 = Teacher('Алексеева', 'Алена', 'Алексеевна', [3], ['6А', '7А'])
teacher_5 = Teacher('Игнатьева', 'Валентина', 'Игнатьевна', [4], ['7А'])
teachers = [teacher_1, teacher_2, teacher_3, teacher_4, teacher_5]

student_1 = Student('Иванов', 'Иван', 'Иванович', '5А', 'мама1', 'папа1')
student_2 = Student('Петров', 'Петро', 'Петрович', '5Б', 'мама2', 'папа2')
student_3 = Student('Сидоров', 'Сидор', 'Сидорович', '6А', 'мама3', 'папа3')
student_4 = Student('Иванов', 'Алексей', 'Алексеевич', '7А', 'мама4', 'папа1')
student_5 = Student('Иванов', 'Антон', 'Антонович', '7А', 'мама3', 'папа1')
student_6 = Student('Петров', 'Артем', 'Татьянович', '5А', 'мама1', 'папа2')
student_7 = Student('Антонов', 'Иван', 'Иванович', '5Б', 'мама5', 'папа4')
student_8 = Student('Сидоров', 'Иван', 'Иванович', '6А', 'мама6', 'папа3')
students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8]

school = School('Гимназия', 'Москва, ул. Ленина', teachers, students, courses, classrooms)
print('Классы: {0}'.format(', '.join(school.get_classrooms())))
print('Студенты в {0}: {1}'.format('5А', ', '.join(school.get_students_in_class('5А'))))
print('Курсы для {0}: {1}'.format(student_1.short_name, ', '.join(school.get_courses_for_student(student_1))))
print('Курсы для {0}: {1}'.format(student_5.short_name, ', '.join(school.get_courses_for_student(student_5))))
print('Студент {0}, родители: {1}, {2}'.format(student_1.short_name, student_1.parents['mother'],
                                                                    student_1.parents['father']))
print('Учителя в 5А:', ', '.join(list(map(str, school.get_teachers_in_class_room('5А')))))
