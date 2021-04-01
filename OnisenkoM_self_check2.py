"""
Онищенко Михаил Сергеевич
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
s = 'Онищенко Михаил Сергеевич'
i = 14

""" +++ ВЛОЖЕННЫЕ СПИСКИ +++ """

""" Задание №1
Создайте пустой список 'fio'
---------------начало блока редактирования----------------"""

fio = []

"""------------ конец блока редактирования----------------"""
print('№1 ' + str(fio == []))

""" Задание №2
Используя цикл for добавьте в 'fio' список букв вашей фамилии, список букв вашего имени и список букв вашего отчества
---------------начало блока редактирования----------------"""

a = s.split(' ')
for letter in a:
    fio.append(list(letter))

"""------------ конец блока редактирования----------------"""
print('№2 ' + str(fio == [['О', 'н', 'и', 'щ', 'е', 'н', 'к', 'о'], ['М', 'и', 'х', 'а', 'и', 'л'], ['С', 'е', 'р', 'г', 'е', 'е', 'в', 'и', 'ч']]))

""" Задание №3
Используя цикл while переверните каждый элемент в 'fio' задом наперёд
---------------начало блока редактирования----------------"""

while fio:
    fio[0] = fio[0][::-1]
    fio[1] = fio[1][::-1]
    fio[2] = fio[2][::-1]
    break

"""------------ конец блока редактирования----------------"""
print('№3 ' + str(fio == [['о', 'к', 'н', 'е', 'щ', 'и', 'н', 'О'], ['л', 'и', 'а', 'х', 'и', 'М'], ['ч', 'и', 'в', 'е', 'е', 'г', 'р', 'е', 'С']]))

""" Задание №4
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][3]

"""------------ конец блока редактирования----------------"""
print('№4 ' + str(char == 'х'))

""" Задание №5
Получите из переменной fio 3-ю букву вашего имени и запишите её в в переменной 'char'
---------------начало блока редактирования----------------"""

char = fio[1][3]

"""------------ конец блока редактирования----------------"""
print('№5 ' + str(char == 'х'))

""" Задание №6
Создайте список fio_len и запишите в него длины вашей фамилии, имени и отчества, получив их из fio
---------------начало блока редактирования----------------"""

fio_len = []
fio_len.append(len(fio[0]))
fio_len.append(len(fio[1]))
fio_len.append(len(fio[2]))

"""------------ конец блока редактирования----------------"""
print('№6 ' + str(fio_len == [8, 6, 9]))

""" Задание №7
Используя стандартную функцию min получите длину самого короткого слова из ваших ФИО
---------------начало блока редактирования----------------"""

min_len = min(fio_len)

"""------------ конец блока редактирования----------------"""
print('№7 ' + str(min_len == 6))

""" Задание №8
Используя цикл в цикле получите строку, в которой будет:
последняя буква вашей фамилии, затем имени, затем отчества,
затем предпоследния буква вашей фамилии, имени, отчества,
затем предпредпоследния буква вашей фамилии, имени, отчества,
и так до того момента, пока не закончатся символы в самом коротком слове из вашей ФИО
---------------начало блока редактирования----------------"""

chars = None

"""------------ конец блока редактирования----------------"""
print('№8 ' + str(chars == 'олчкиинавехещиеиМг'))


""" +++ СЛОВАРИ +++ """

""" Задание №9
Создайте словарь с ключами 'фамилия' 'имя' 'отчество' и соответствующими значениями ФИО задом наперёд
---------------начало блока редактирования----------------"""

a = dict()
a['фамилия'] = fio[0]
a['имя'] = fio[1]
a['отчество'] = fio[2]
reversed_fio_dict = a
"""------------ конец блока редактирования----------------"""
print('№9 ' + str(reversed_fio_dict == {'фамилия': ['о', 'к', 'н', 'е', 'щ', 'и', 'н', 'О'], 'имя': ['л', 'и', 'а', 'х', 'и', 'М'], 'отчество': ['ч', 'и', 'в', 'е', 'е', 'г', 'р', 'е', 'С']}))

""" Задание №10
Получите список ключей словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_keys = list(reversed_fio_dict.keys())

"""------------ конец блока редактирования----------------"""
print('№10 ' + str(reversed_fio_dict_keys == ['фамилия', 'имя', 'отчество']))

""" Задание №11
Получите список значений словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_values = list(reversed_fio_dict.values( ))

"""------------ конец блока редактирования----------------"""
print('№11 ' + str(reversed_fio_dict_values == [['о', 'к', 'н', 'е', 'щ', 'и', 'н', 'О'], ['л', 'и', 'а', 'х', 'и', 'М'], ['ч', 'и', 'в', 'е', 'е', 'г', 'р', 'е', 'С']]))

""" Задание №12
Получите список картежей, содержащий пары ключ и значение словаря reversed_fio_dict
---------------начало блока редактирования----------------"""

reversed_fio_dict_items = list(tuple(reversed_fio_dict.items()))

"""------------ конец блока редактирования----------------"""
print('№12 ' + str(reversed_fio_dict_items == [('фамилия', ['о', 'к', 'н', 'е', 'щ', 'и', 'н', 'О']), ('имя', ['л', 'и', 'а', 'х', 'и', 'М']), ('отчество', ['ч', 'и', 'в', 'е', 'е', 'г', 'р', 'е', 'С'])]))

""" Задание №13
Получите значение словаря reversed_fio_dict по ключу фамилия
---------------начало блока редактирования----------------"""

res = reversed_fio_dict.get('фамилия')

"""------------ конец блока редактирования----------------"""
print('№13 ' + str(res == ['о', 'к', 'н', 'е', 'щ', 'и', 'н', 'О']))

""" Задание №14
Создайте пустой словарь chars
---------------начало блока редактирования----------------"""

chars = {}

"""------------ конец блока редактирования----------------"""
print('№14 ' + str(chars == {}))

""" Задание №15
Преобразуйте строку с вашей ФИО так, чтобы в ней были только маленькие буквы и отсутствовали пробелы
---------------начало блока редактирования----------------"""

s = s.replace(' ', '').lower( )

"""------------ конец блока редактирования----------------"""
print('№15 ' + str(s == 'онищенкомихаилсергеевич'))

""" Задание №16
Пройдите в цикле по всем буквам своих ФИО 's' и сосчитайте количество повторений каждой буквы.
Получите список 'res' из пар (кортежей):
( <буква вашей ФИО>, <количество её появления в вашей ФИО> )
---------------начало блока редактирования----------------"""

a = {}
for i in s:
    a[i] = 0
for i in s:
    if i in a.keys():
        a[i] += 1
res = list(tuple(a.items()))

"""------------ конец блока редактирования----------------"""
print('№16 ' + str(res == [('о', 2), ('н', 2), ('и', 4), ('щ', 1), ('е', 4), ('к', 1), ('м', 1), ('х', 1), ('а', 1), ('л', 1), ('с', 1), ('р', 1), ('г', 1), ('в', 1), ('ч', 1)]))


""" +++ ФУНКЦИИ +++ """

""" Задание №17
Напишите функцию mihailCharToIndex которая:
- получает на вход букву русского алфавита,
- возвращает её номер в алфавите (от 1 до 33).
Например вызов mihailCharToIndex('А') должен возвращать 1
---------------начало блока редактирования----------------"""

def mihailCharToIndex(letter):
    alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    return alphabet.index(letter)+1

"""------------ конец блока редактирования----------------"""
print('№17 ' + str(mihailCharToIndex("С") == 19))

""" Задание №18
При помощи функции mihailCharToIndex измените fio так, чтобы вместо букв, в нём были их номера в алфавите
---------------начало блока редактирования----------------"""

fio = None

"""------------ конец блока редактирования----------------"""
print('№18 ' + str(fio == [[16, 12, 15, 6, 27, 10, 15, 16], [13, 10, 1, 23, 10, 14], [25, 10, 3, 6, 6, 4, 18, 6, 19]]))


""" +++ КОНЕЦ =) +++ """
