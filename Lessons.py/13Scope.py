'---------ОБЛАСТИ ВИДМОСТИ-----------'
#LEGB - Local Enclosed Global Build-in

'---------Build In---------------'
#встроенное пространство имен(print, list, sum, input)

'---------Global---------------'
#все переменные, которые мы создали внутри одного файла
#чтобы посмотреть глобальные переменные можно использовать globals
# a = 5
# b = 6
#print(globals())

'-----Enclosed(non local)----------'
#Замкнутое прсотранство имен - локальное пространство, 
#у которого есть внутренне локальное пространство.
# var = 'global'
# def func():
#     var = 'enclosed'
#     def inner_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()
'------------Local----------------'
#Локальное пространство имен - переменные, созданные функции внутри
#Пример 1
# a = 10 #это глобальная переменная
# def func(a,b): #здесь а это локальная переменная
#     print('Global',globals())
#     print('Local',locals())
#     print(a,b)
# func(5,7)

#Пример 2
# count_1 = 1
# def count1():
#     print(count_1)
# count1()

#Пример 3
# def counter(i):
#     count_ = 0

#     def inner_counter():
#         nonlocal count_ #доступ на изменение переменной замкнутого пространства
#         print(count_)
#         count_ += 1

#     for _ in range(i):
#             inner_counter()

# counter(10)

'----------Работа с файлами------------'
#open - функция, которая открывает файл в определенном режиме
""" 
Режимы
"""
# r - read(только для чтения)
# w - write(только для записи, каждый раз файл очищатеся)
# a - append(только добавление записи, добавляется в конец файла)
# x - создает файл, но если он уже существует выйдет ошибка
# b - binary (открывает файл в бинарном виде)

# new_file = open('test2.txt', 'x')
# print(dir(new_file))
# new_file.close() #вызывают какую либо команду

'-------------Read-----------'
# file = open('test2.txt', 'r')
# # print(file.read())
# # print(file.writable()) # метод который проверяет, можно ли что то написать в файл
# # print(file.readable()) # метод проверяет ли прочитать файл

# # file.seek(0)
# # print(file.read())

# # print(file.readline()) #выводит только строку документа, возвращает строку, можно использовать методы строк
# print(file.readline(2)) #выводит только 2 первых символа
# print(file.readline().replace('\n',''))
# print(file.tell()) #смотрит расположение курсора
# file.close() #обязательно пишем close чтобы избежать ошибку

'------------Write--------------' # очищает информацию
# file = open('test2.txt', 'w') # очищение файла происходит при открытии
# # print(file.readable())
# # print(file.writable())
# # file.write('Ada courses') # перед ем как записать файл очищается полностьб
# file.writelines(['bootcamp', 'truckers', 'terminator'])
# file.close()

'-------------Append----------' # при этом оставляет информацию, не очищает файл
# file = open('test2.txt', 'a') #если файла нету, то он его создаст
# file.close()

'------Контекстный менеджер---------'
#конструкция with работает с любыми объектами, у которых есть два метода
#__enter__, __exit__
#__enter__  работает в начале конструкции wuth (try)
#__exit__  работает когда конструктор закончил работу и заканчивается конструкция через finally

# with open('test2.txt', 'w+') as file: #w также очищает файл
#     print(file.readable())
#     print(file.writable())
#     file.write('1,2,3,4,5')
#     print(file.tell())
#     file.seek(0)
#     print(file.read())

'------Задания-------'
""" 
Создайте файл, внесите туда небольшой текст. В программе
откройте этот файл и выведите содержимое на экран.
"""
# with open('test3.txt', 'w+') as file:
#     file.writelines(['Otto','Dusseldorf', 'Jagtpanzer'])
#     file.seek(0)
#     print(file.read())

""" 
Создайте файл users.txt. Напишите программу которая
спрашивает у пользователя его Логин и Пароль и записывает в
файл users.txt.
"""
# name=input('Введите имя: ')
# password=input('Введите пароль: ')
# with open('users.txt','w+') as file:
#     file.write(name+'\n')
#     file.write(password)
#     print(file.read())
