'----------------Встроенные функции-------------'
#map, filter, zip, enumerate

#zip - соединяет несколько последовательностей (получаем генераторб в котором элементы tuple)
# list1=[1,2,3,4,5,6]
# list2=['a','b','c']
# list3=[1.5,1.2,1.3]
# zippend=zip(list1,list2,list3)
# # print(zippend) #получим непонятные объекты, поэтому нужно:
# for elem in zippend:
#     print(elem)

#таким же образом создадим словарь
# dict_=dict(zip(list2,list3))
# print(dict_)

# #enumerate - нумерует последовательность (по дефолту с 0) так же получаем генератор
# enumerated=enumerate('hello')
# # print(enumerated) #получим непонятные объекты, поэтому нужно:
# print(list(enumerated))

#map - функция высшего порядкаб она принимает другую функцию и итерируемый объект, 
# выполняет заданную функцию на каждый элемент последовательности
# list1=['1','2','3']
# mapped=map(int,list1)
# print(list(mapped))

# number=map(int,input('Введите числа через пробел: ').split()) #split делит элементы и закидывает их в лист
# print(f'Sum numbers={sum(list(number))}') #здесь f для форматирования строки

#filter - функция высшего порядка, возвращает генератор, с элеметами,
#прошедшими фильтр(какое-то условие), принимает функцию и последовательность.
# list1=[1,2,3,-3,-2,-1,0]
# filtered=filter(lambda i : i>0, list1)
# print(filtered) #получим непонятные объекты, поэтому нужно:
# print(list(filtered))

# string=input('Введите слова через пробел: ').split()
# result=list(map(len,string)) #преобразовать слова в элементы т.е вывести списки длин
# print(string)
# print(result)

# nums=[1,2,3,4,55,66,77,8,79]
# # res=filter(lambda i:i<5, nums) #результат через filter
# # print(list(res))

# # res=[i for i in nums if i<5]
# # print(res)

# nums=[1,2,3,4,55,66,77,8,79]
# def find_even():
#     for num in nums:
#         if num % 2 == 0:
#             print(num) #нужно вызвать код с помощью нижней команды (покажет четные числа)
# find_even()

# nums=[1,2,3,4,55,66,77,8,79]
# nums1=[234,55,89]

# def find_even():
#     for num in nums:
#         if num % 2 == 0:
#             print(num) #нужно вызвать код с помощью нижней команды (покажет четные числа)
# find_even()

# snake_case (PEP-8) используется для логического названия объектов
# my_phone = 'samsung'
# numbers=8

'------------Функция --------------'
#Функция - это именованный блок кода, который вызывается множество раз в друших частях программы
#Она создается командой def
#При наименовании функции нужно придерживаться стиля Snake_case (наименованию через "_")
# snake_case (PEP-8) используется для логического названия объектов

# def our_sum(num1,num2):
#     res=num1+num2
#     return res
# print(our_sum(5,6)) #получим результат 11