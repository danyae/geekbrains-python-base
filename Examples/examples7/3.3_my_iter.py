Под катом шпаргалка, в которой очень вкратце описано зачем и как создавать и использовать генераторы.

Введение

Самый наверное распространенный тип цикла в питоне такой:

1 for element in <iterator object> 
2     print element
3     
 
В этом скрипте в качестве "iterator object" может выступать список, словарь, открытый файл,в общем любой итератор.

Предположим, мы хотим обработать набор каких-то данных. Обычно схема действий такова:

Создаем список, элементами которого являются данные, которые нам нужно обработать.
Обрабатываем элементы списка в цикле "for...in"
Но не всегда удобно действовать по такой схеме. Например, встретилась одна из следующих ситуаций:

Очень большой набор данных. Работать будет, но при этом займет много времени и оперативной памяти.
Большое время на получение одного элемента набора. Придется ждать, пока получим все данные набора, иногда это может занять немаленькое время. Предположим, нам нужно только несколько первых значений большого набора, а мы получаем или вычисляем все значения.
В таких случаях хорошо бы вычислять очередное значение только тогда, когда оно нам понадобится, а не вычислять все значения заранее. Это можно осуществить тремя путями:

Создать объект-итератор.
Создать функцию-генератор.
Использовать генераторное выражение.
Итераторы

Добавлено в Python 2.2

Чтобы получить объект-итератор, нужно создать объект, который будет иметь два метода со специальными именами:

__iter__() - метод, который возвращает сам объект.
next() - метод, который возвращает следующее значение итератора.
Пример итератора

Предположим, что нам нужно сделать объект, который берет данные из строк очень большого файла. Данные нужны порциями, которые записаны в строках текстового файла, одна порция, одна строка. Обрабатывать нужно в цикле "for...in"

Создаем такой класс:

 1 class SimpleIterator(object):
 2     
 3     def __init__(self,fname):
 4         self.fd = open(fname,'r')
 5         
 6     def __iter__(self):
 7         return self
 8 
 9     def next(self):
10         l = self.fd.readline()
11         if l != '':
12             l = l.rstrip('\n')
13             num = int(l)
14             return num*2
15         raise StopIteration

Файл данных:

3
4
Внутри все очень просто. Главная работа в методе next(). В нем считывается следующая строка файла, обрабатывается (число умножается на 2) и возвращается в операторе return(). Когда файл окончится будет вызвано исключение StopIteration.

Проверка:

1 >>> simple_iter = SimpleIterator('test_data.txt')
2 >>> for i in simple_iter:
3 ...    print i
4 6
5 8

Генераторы

Добавлено в Python 2.2/2.3

Генератор, это очень похоже на итератор, только это функция. При вызове этой функции в цикле, она при каждом новом цикле выдает следующее значение. Пишется эта функция с использованием оператора yield

yield работает как return, с одной разницей, что между вызовами функций, все состояния и данные будут при следующем вызове функции такими, какими они были на момент предыдущего исполнения yield.

По сути это ключевое слово создает итератор, просто создание итератора упрощается за счет того, что методы __iter__() и next() создаются автоматически. При выходе из функции не по оператору yield автоматически генерируется StopIteration.

Пример создания генератора

Создать функцию генератора очень просто. Пишем функцию, которая возвращает в операторе yield данные.

1 def power(start):
2     print "power is called the first time"
3     for i in xrange(start,start+5):
4         yield i*i
5     print "power is called the last time"

Как видим, yield вызывается внутри цикла. Строки 2 и 5 вставлены для того, чтобы продемонстрировать то, что в этих местах код будет вызываться однократно. Строка 2 при первом вызове функции, строка 5 - при последнем вызове.

Результат работы:

1 >>> power(5)
2 power() is called the first time
3 4
4 9
5 16
6 25
7 36
8 power() is called the last time

Генераторные выражения

Добавлено в Python 2.4

Иногда, в простых случаях, можно не писать функцию-генератор, а обойтись генераторным выражением. Это такой синтаксис для создания простого генератора прямо в том месте, где это нужно.

Синтаксис такой:

1 (expr1 expr2)

Где нужно учесть следующее::

Выражение всегда заключено в круглые скобки.
В случае, если выражение используется в качестве единственного аргумента при вызове функции, круглые скобки выражения могут совпадать с круглыми скобками вызова функции.
expr2 - итератор, генерирующий значения.
expr1 - операция, которая производится с сгенрированным expr2 значением.
Таким образом, генераторное выражение работает следующим образом:

При очередном вызове expr2, и генерирует следующее исходное значение.
Сгенерированное исходное значение подставляется в expr1.
Сгенерированное expr1 значение возвращается генераторным выражением.
Генераторное выражение ждет следующего вызова
Простейший пример:

1 >>> for i in (x*x for x in [1,5,8]):
2 ...    print i

Выражение напечатает квадраты чисел 1,5,8

Еще пример:

1 >>> print sum(x*(5+x) for x in xrange(10,20))

Выражение напечатает сумму результатов вычисления выражения x*(5+x), при x принимающем целочисленные значения от 10 до 20,

Использованные термины

Английский	Русский	Произношение
Iterator	Итератор	Итэрейтэ
Generator	Генератор	джЕнерейтэ
Generator expression	Генераторное выражение	джЕнерейтэ экспрЭшен
yield	давать, приносить, доход	йЕлд
