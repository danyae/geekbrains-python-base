# https://www.programiz.com/python-programming/methods/built-in/classmethod
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()




from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))



# иногда нужно модифицировать аттрибуты класса, а не экземпляра (уже после его создания).
# >>> class A:
# ...     foo = 'foo'
# ...     @classmethod
# ...     def change_foo(cls, value):
# ...             cls.foo = value
# ...
# >>> a = A()
# >>> b = A()
# >>> a.foo
# 'foo'
# >>> a.foo = 'foo?' #добавит аттрибут экземпляра, который спрячет за собой аттрибут класса
# >>> a.foo #как видим, аттрибут изменен
# 'foo?'
# >>> b.foo #однако для другого экземпляра аттрибут foo остался неизменным
# 'foo'
# >>> a.change_foo('foo?')#здесь меняем аттрибут класса
# >>> b.foo
# 'foo?'