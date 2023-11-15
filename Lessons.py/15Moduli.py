# import calculator

# a = calculator.add(5,10)
# print(a)

# a = calculator.substract(5,10)
# print(a)

# a = calculator.divide(5,10)
# print(a)

# a = calculator.multiply(5,10)
# print(a)

#показывает в какой директории мы находимся
# import os
# pwd = os.getcwd()
# print('Текущая директория', pwd)

#показывает содержимое директории
# ls = os.listdir()
# print('Содержимое текущей директории', ls)

#Создание новой папки
# os.mkdir('Новая папка')

#удаление файла
# os.remove('')

# def hello(name):
#     text = f'Hello {name}'
#     return text

# if __name__=='__main__':
#     print(hello('ADA'))

# from .my_package import calculator
# print(calculator.add(5,5))def hello(name):
#     text = f'Hello {name}'
#     return text

# if __name__=='__main__':
#     print(hello('ADA'))

'-----------МОДУЛИ-----------'
#Любой файл с расширением .ру = модуль
#Пакет - набор модулей (обязательно должен быть файл __init__.py (перед init обязательно пробел))

'--------Pip, venv------------'
# pip - это установщик пакетов (pip install название пакета)
# venv - это виртуальное окружение (изолированное пространство), куда мы скачиваем пакеты, библиотеки, модули.

#Установка виртуального окружения происходит через команду "python3 -m venv" название виртуального окружения
#Чтобы активировать виртуальное окружение нужно прописать команду "source venv/bin/activate"

#pip list - показывает все установленные пакеты

'--------ЗАДАНИЯ------------'
"""
Напишите функцию get_info которая запрашивает у пользователя имя и фамилию последовательно.
Далее внутри get_info вызовите другую функцию generate_password которая будет
генерировать пароль при помощи конкатенации имени и фамилии пользователя
и рандомных 7 чисел (от 0 до 9). В конце get_info возвращает пользователю сгенерированный пароль.
"""
# import random
# def generate_password(name,surname): #вызываем функцию передавая ей имя и фамилию пользователя
#     random_number=random.sample(range(1,10),k=7) #с помощью рандом она генерирует числа от 0 до 7 контактируя с именем и фамилией
#     print(random_number)
#     random_number = [str(i) for i in random_number]
#     password = name + surname + ''.join(random_number)
#     return password #для каждой команды свой return

# def get_info(): #запрашиваем у пользователя инфу
#     name = input('Введите имя: ')
#     surname = input('Введите фамилию: ')
#     password = generate_password(name, surname) #здесь она возвращает сгенерированный пароль
#     return password 
# print('Ваш пароль:',get_info ())

"""
Из списка имён names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan','ISA', 'Emir', 'Ilim'], 
достаньте 3 рандомных имени и запишите в другой список.
"""
#ВАРИАНТ 1
# names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
# new_names = []
# import random
# random_index = random.sample(range(len(names)),3)
# random_names = [names[i] for i in random_index]
# new_names.extend(random_names)
# print(new_names)

#ВАРИАНТ 2
# i = 0
# while i<3:
#     import random
#     names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
#     l = random.randint(0,len(names))
#     a = names.pop(l-1)
#     print(a)
#     i += 1

#ВАРИАНТ 3
# import random
# def ran():
#     names = ['Beka', 'Alymbek', 'Aziz', 'Nursultan', 'Timur', 'Dastan', 'ISA', 'Emir', 'Ilim']
#     import random
#     for i in range(1,4):
#         a = random.choice(names)
#         print(a)
# ran()

"""
Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.
"""
# import sys
# operation_system = sys.platform
# print(operation_system)

"""
Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте какое из 2-х значений занимает больше памяти.
"""
# import sys
# linux = sys.platform
# print('Os',linux)
# s1 = input("Значение 1: ")
# s2 = input('Значение 2: ')
# string_1 = sys.getsizeof(s1)
# string_2 = sys.getsizeof(s2)
# print(f'Первая строка занимает {string_1} байт')
# print(f'Вторая строка занимает {string_2} байт')

"""
Создайте программу которая спрашивает у пользователя число N для генерации пароля а затем генерирует ему пароль длиною N символов.
"""
# import random
# import string
# def generate_password(len): #здесь len желаемая длина пароля
#     digits = string.digits
#     letters = string.ascii_letters
#     data = digits+letters
#     password = ''.join(random.choice(data)for i in range(len))
#     return password
# n = int(input('Введите длину пароля: ')) #запрашиваем у пользователя информацию
# password = generate_password(n)
# print(password)

"""
Создайте игру Камень-Ножницы-Бумага с Компьютером. Где компьютер даёт вам выбрать опцию,
а сам затем генерирует своё значение. По итогу говорит выиграли вы, проиграли или ничья.
"""
#Вариант 1
# def ch(choi):
#     import random
#     cm_choice = ['Камень','Ножницы','Бумага']
#     rand = random.choice(cm_choice)
#     if choi == rand:
#         print('Invalid')
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     elif (choi == 'Камень' and rand == 'Ножницы') or (choi == 'Ножницы' and rand == 'Бумага') or (choi == 'Бумага' and rand == 'Камень'):
#         print("You win")
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     else:
#         print("Кпц ты лох лол")
#         print(f'Your choice: {choi}')
#         print(f'Comp choice: {rand}')
#     return game()

# def game():
#     while True:
#         choice = input('Ваш выбор: Камень|1, Ножницы|2, Бумага|3 Выход|4   : ')
#         if choice == '1':
#             stone = "Камень"
#             print(ch(stone))
#         if choice == '2':
#             scissor = 'Ножницы'
#             print(ch(scissor))
#         if choice == '3':
#             paper = 'Бумага'
#             print(ch(paper))
#         if choice == '4':
#             print("Вы покинули игру!")
#             break
# game()

#Вариант 2
# import random
# choice = ['камень', 'бумага' , 'ножницы']
# def play_2():
#     while True:
#         you = input('Сделайте выбор: камень ножницы или бумага: ')
#         laptor = random.choice(choice)
#         print(f"\n Вы выбрали {you}, ноутбук выбрал {laptor}.")
#         if you == laptor:
#             print(f'Оба выбрали {you} Ничья!')
#         elif you == "камень":
#              if laptor == "ножницы":
#                  print('Камень бьет ножницы! Вы победили!' )
#              else:
#                  print('Бумага оборачивает камень! Вы проиграли.')
#         elif you == 'бумага':
#             if laptor == 'камень':
#                 print('Бумага оборачивает камень! Вы победили!')
#             else:
#                 print('Ножницы режут бумагу! Вы проиграли')
#         elif you ==  'ножницы':
#             if laptor == 'бумага':
#                 print('Ножницы режут бумагу! Вы победили!')
#             else:
#                 print('Камень бьет ножницы! Вы проиграли.')
#             play_again= ""
#             play_again = input('Сыграем еще? (д/н): ')
#             if play_again.lower() != "д":
#                 break
# play_2()

