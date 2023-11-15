"------------------------Двумерные списки(массивы)--------------------"
# Двумернык списки - это структура данных, которая представляет собой таблицу, состоящию из строк и столбцов.
# В python двумерные массивы реализуются с помощью вложенных списков.

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix)
'-----------------While matrix-----------------'
# n = 3 # количество строк
# m = 3 # количество столбцов
# array = []
# count = 1
# i = 0
# while i < n:
#     array.append([])
#     j = 0
#     while j < m:
#         array[i].append(count)
#         count += 1
#         j += 1
#     i += 1
'-----------------------For matrix--------------------'
# n = 3
# m = 3
# array = []
# count = 1
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append(count)
#         count +=1

# n = 3
# m = 5
# array = list(range(n))
# print(array)
# for i in range(n):
#     array[i] = list(range(1, m+1))
# print(array)

# matrix = [
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5,6,7,9],
#     [1, 2, 3, 4, 5]
# ]
# n = len(matrix)
# m = len(matrix[0])
# i = 0
# while i < n:
#     j= 0
#     while j < m:
#         print(matrix[i][j], end='  ')
#         j += 1
#     print()
#     i += 1
# print(matrix)
# matrix = [
#     [1, 2, 3, 4, 5],
#     [1, 2, 3, 4, 5, 6, 7, 9],
#     [1, 2, 3, 4, 5]
# ]
# n = len(matrix)
# for i in range(n):
#     m = len(matrix[i])
#     for j in range(m):
#         print(matrix[i][j], end='  ')
#     print()

# print(matrix)
# n = 3
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i] = list(range(m))
#     for j in range(m):
#         el = input('Введите элемент в {} x {} позицию '.format(i, j))
#         array[i][j] = el

# print(array)

# list1 = []
# for i in range(1,6):
#     list1.append(i)
# print(list1)

# list2 = [i for i in range(1,6)]
# print(list2)
# '------------------------Comprehensions-----------------------------'
# # Генератор - c помощью которого мы можем создавать последовательность используя цикл for в одну строку.
# """
# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр
# результат if условие else тело for элемент in последовательность
# результат if условие else тело for элемент in последовательность if фильтр
# """
# comperhensions_ = (i for i in range(10) if i % 2 ==0)
# print(comperhensions_)
# print(type(comperhensions_))
# for i in range(3):
#     print(next(comperhensions_)) # 0

# # next - функцию, которая запрашивает у генератора текущий элемент и генератор создают следующий элемент

# '-----------------------List Comperhensions------------------------'
# list1 = [i for i in range(10)]

# new_list = [1, 'hello', True, 2, False, 'sdfad', 'adfasdfasdf']
# string = [i for i in new_list if type(i) == int]
# print(string)

# '-----------------------Dict Comperhensions------------------------'
# dict_ = {i:i for i in range(10)}
# print(dict_)

# dict_ = {'a': [1,2,3,4,5], 'b': [2,3,4,5,6], 'c': [2,3,5,7]}
# new_dict = {key:sum(val) for key, val in dict_.items()}
# print(new_dict)

# '------------------------Set Comperhensions----------------------'
# set1 = [1,2,3,4,4,5,3,2,1]
# set_ = {i for i in set1}
# print(set_)
'------------------ЗАДАНИЯ--------------'
"""
Создайте двумерный список размера 3x4 с помощью вложенных
циклов заполните единицами.
"""
#Вариант1
# n=4
# m=3
# matrix=[]
# count=1
# for i in range(n):
#     matrix.append([])
#     for j in range(m):
#         matrix[i].append(count)
# for i in matrix:
#     print(i)

#Вариант2
# n=4
# m=3
# matrix=[[1]*m for i in range(n)]
# print(matrix)

"""
# 4) Составьте таблицу умножения чисел от 1 до 5(включительно)
"""
# table=[[0]*5 for _ in range(5)]
# for i in range(1,6):
#     for j in range(1,6):
#         table[i-1][j-1]-i*j
# for row in table:
#     print(row)
"""
# 5) Составьте таблицу умножения чисел от 1 до 5(включительно)
"""
# n = 10
# m = 5
# array = []
# count = 1
# for i in range(n):
#     array.append([])
#     array[i].append([number*count for number in range(1,6)])
#     count +=1
# print(array)
"""
Составьте шахматную доску заполненная символами '.', "*".
В левом верхнем углу должна стоять '.'
"""
#Вариант1
# n=8
# m=8
# chess_board=[]
# for i in range(n):
#     row=[]
#     for j in range(m):
#         if(i+j ) % 2 ==0:
#             row.append('.') #надо чтобы начиналось (была) с точки
#         else:
#             row.append('*') #символ умножить
#     print(row)
#     chess_board.append(row)
#Вариант2
# n=8
# m=8
# chess_board=[]
# for i in range(n):
#     row=[]
#     for j in range(m):
#         if(i+j ) % 2 ==0:
#             row.append('.') #надо чтобы начиналось (была) с точки
#         else:
#             row.append('*') #символ умножить
#     for row in chess_board:
#         print(' '.join(row))

'------СЛОВАРИ В ПАЙТОН----------'
"""
В словарях в пайтон словари имеют значение ключи и значения.
Ключи являются неизменяемыми, а значения изменяемыми.
Ключ и значение разделяются двоеточием,
Пара ключ-значение запятой
Словарь разделяется фигурными скобками
"""
# student_ages = dict(Amanda=27, Teresa=25, Alex=22)
# print(student_ages)

#комбинированый метод
# student_ages = dict({'Amanda': 27, 'Teresa': 25}, Alex = 22)
# print(student_ages)

#использование списка кортежей
# student_ages = dict([('Amanda', 27), ('Teresa', 25,), ('Alex', 25)])
# print(student_ages)

#Создание словаря, используя два списка. Вначале строим итератор
#кортежей с помощью функции zip(). Затем используем ту же
#функцию dict() для построения словаря.
# students = ['Amanda', 'Teresa', 'Alex']
# ages = [27, 25, 22]
# students_ages = dict(zip(students,ages))
# print(students_ages)

# country = {'code': 'RU', 'name': 'Russian Federation', 'population': '144'}
# for key, value in country.items():
#     print(key, "-", value)

#удаление элемента через pop
# country = {'code': 'RU', 'name': 'Russian Federation', 'population': '144'}
# country.pop('name')
# print(country)

#удаление последнего элемента через popitem
# country = {'code': 'RU', 'name': 'Russian Federation', 'population': '144'}
# country.popitem()
# country.popitem() #если запустить повторно то удалит еще 1 элемент
# print(country)

#получение только ключей
# country = {'code': 'RU', 'name': 'Russian Federation', 'population': '144'}
# print(country.keys())

#получение только значений
# country = {'code': 'RU', 'name': 'Russian Federation', 'population': '144'}
# print(country.values())


