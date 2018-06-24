# как сделать объект класса итерируемым, хороший способ если в self._peoples небольшое количество объектов.
class People:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class ClassRoom:
    people = People

    def __init__(self):
        self._peoples = [self.people('name', 'surname') for _ in range(10)]

    def __len__(self):
        return len(self._peoples)

    def __getitem__(self, position):
        return self._peoples[position]


class_room = ClassRoom()
for student in class_room:
    print(student.name)



