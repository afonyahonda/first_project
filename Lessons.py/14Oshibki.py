'-----------Вызов исключений--------'
#raise SyntaxError
'-----------Обработка исключений----------'
#Чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except и обработать вызванное исключение
#ПРИМЕР1
# try: #самая главная функция(как elif не сработает без if)
#     #код который возможно вызовет ошибку
#     num = int(input('Введите число: '))
# except ValueError: #исключение, которое может возникнуть 
#     print('Вы ввели не число!')
# else: #код который выполнится, если нет ошибок
#     print('Вы ввели число', num)
# finally: #код который выполнится в любом случае
#     print('Финал')

#ПРИМЕР2
# try:
#     num = int(input('Введите число: '))
#     if num == 0:
#         raise ValueError #с помощью Except мы вызываем ошибку
# except ValueError: #с помощью except мы отлавливаем ошибку
#     print('Вы ввели ноль')

#ПРИМЕР3
# try:
#     a = int(input())
#     k = 10/a
#     raise Exception #с помощью Except мы вызываем ошибку
# except: #с помощью except мы отлавливаем ошибку
#     print('Отловлена любая ошибка')

"""
Напишите программу которая будет получать через input 2 числа num1, num2 и будет печатать их сумму.
Обработайте ошибку, которая возникнет если пользователь введет что-то кроме числа и выведет сообщение: 'Введите число'
"""
# def our_sum():
#     try:
#         num1=int(input('Введите число 1: '))
#         num2=int(input('Введите число 2: '))
#         print(f'(num1) + (num2) = {num1+num2}')
#     except ValueError:
#         print('Введите число!')

#our_sum()
# a,b = 1,0
# try:
#     print(a/b)
#     print('Это сообщение не будет напечатано')
#     print(10+'10')
# except TypeError:
#     print('Вы сложили значение несовместимых видов')
# except ZeroDivisionError:
#     print('Деление на 0')

# try:
#     print(a/b)
# except:
#     print('Деление на 0')
# print('Будет ли это сообщение напечатано?')

# try:
#     print('1'+1)
#     print(name)
#     print(1/0)
# except NameError:
#     print('name не существует')
# except (ZeroDivisionError, TypeError): #можно вызвать сразу несколько ошибок
#     print('Деление на 0')
# except:
#     print('Что-то пошло не так')

'-----------Assert(Утверждение)------------'
#Assert в Python используется для проверки утверждения или условий в коде. Он представляет собой
#способ убедиться, что определенное условие верно! И если оно не выполняется, генерируется исключение AssertError

# a = 0 
# assert a == 0, 'Сообщение об ошибке'
# print(a)

'Создайте функцию divide(), которая принимает 2 числа и возвращает результат их деления'
# def divide():
#     try:
#         a = int(input('Введите число a: '))
#         b = int(input('Введите число b: '))
#         print(f'{a}/{b} = {a/b}')
#     except ZeroDivisionError:
#         print('Деление на 0!')
#         divide() #повторяют вызов функций (т.е программа будет запускаться заново)
#     except ValueError:
#         print('Что-то пошло не так!')
#         divide() #повторяют вызов функций (т.е программа будет запускаться заново)
# divide()

"""
Создайте файл с именем data.txt и запишите в него несколлько строк текста.
Затем напишите программу которая пытается открыть этот файл для чтениия и вывода его
содержимого. Используйте try...except чтобы обработать исключение если файл не сущетсвует
и выведите сообщение об ошибке
""" 
# with open('data.txt', 'w') as file:
#     file.write('123text')     #ЗДЕСЬ МЫ СОЗДАЛИ ФАЙЛ
# try:
#         with open('data.txt', 'r') as file:
#             text = file.read()
#             print('Содержимое файла: ')
#             print('text')
# except FileNotFoundError:
#       print('Ошибка: Файла не сущетсвует!')
