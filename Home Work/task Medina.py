
# print('Ты любишь Медину?'.upper())
# answer = input('Введите ваш ответ: ').lower()
# if answer == 'да':
#     print('Правильно')
# else:
#     print('Неправильно')

"""
Что больше или равно числа 17925: (34**2); (26*3); (17*33); (4394*4)
"""
# print(34*2>=17925)
# print(26*3>=17925)
# print(17*33>=17925)
# print(4394*4>=17925)

"""
Что больше:
(17*3) или (12*5) (12**3) или (13*7) (4**5) или(512+512)
"""
# print(17*3>12*5)
# print(12**3>13*7)
# print(4**5>512+512)

"""
Составить выражение:
Сложить 2 любых числа
Умножить их на любое число
Возвести в квадрат
Отнять от всего результат: 193432
"""
# print((25+5)*2**2-193432)

"""
Создать 3 переменные в которых лежат 3 одинаковых числа с плавающей точкой. 
Первые 2 переменные между собой сложить и умножить на 3ю переменную.
"""
# print((4.6+4.6)*4.6)

"""
Создать 5 переменных:
a=Чётное число
b=Любое от 5 до 15
c=Дробное число до 20
d=Любое нечётное число
e=Любое число
Составить следующее выражение:
(a - e ** (b / d)) %c
"""
# a=2
# b=6
# c=12.2
# d=3
# e=8
# print((a-e**(b-d))%c)

"""
Создайте два переменных, в первой год вашего рождения во второй
переменной 2023.
Вычислите свой возраст
Посчитайте сколько должно быть Вам через 2 года
Посчитайте сколько было Вам 2 года назад
Умножьте свой возраст на 365
"""
# birth_year=int(input('Введите год вашего рождения: '))
# current_year=2023
# print('Ваш возраст:',current_year-birth_year)
# print('Через два года вам будет:',current_year-birth_year+2)
# print('Два года назад вам было:',current_year-birth_year-2)

"""
Проверьте являются ли числа 10, 12, 13, 100, 134567 четными числами.
"""
# nums = [10,12,13,100,134567]
# for i in nums:
#     if i % 2 == 0:
#      print('Четное')
# else:
#     print('Нечетное')

"""
Запросите год рождения у пользователя и посчитайте количество прожитых секунд и выведите на экран.
"""
#Вариант1
# age=int(input('Введите год рождения'))
# in_hour = 3600
# in_day = 3600 * 24
# in_year = in_day * 365
# your_age = 2023-age
# print(your_age*in_year)

# Вариант2 с пояснением для пользователя:
# age=int(input('Введите год вашего рождения '))
# in_hour=3600
# in_day=3600 * 24
# in_year=in_day*365
# your_age=2023-age
# print('Вы прожили',your_age*in_year,'секунд')

# ----
# if 13%2==0:
#     print('число четное')
# else:
#     print('число нечетное')

"""
Айтибек в 2020 году весил 75 кг, в 2021г 80 кг, в 2022г 90 и в 2023г 70. 
Выясните насколько похудел или набрал вес Айтибек относительно 2020 года.
"""
# in2020=75
# in2021=80
# in2022=90
# in2023=70
# dif = in2023 - in2020
# if dif > 0:
#     print('Потолстел')
# elif dif < 0:
#     print('Похудел')

# --------
# cost=50
# cost1=50+50*100/100
# print(cost1)

"""
Создайте 2 переменные со значениями 2**3 и 3**2 и покажите значение переменной в которой значение больше.
"""
# a=2**3
# b=3**2
# if a>b:
#     print(a)
# elif b>a:
#     print(b)
# else:
#     print('Они равны')

"""
У нас есть числа от 0 до 100, но не все числа разрешены! 
Разрешенённые: От 0 до 21 или От 57 до 100.
Ввести число и выясните является ли число разрешенным.
"""
# a=int(input('Введите число'))
# if a>0 and a<21 or a>57 and a<100:
#     print('Разрешено')
# else:
#     print('Не разрешено')

"""
Объявите 3 переменные "chocolate", "milk", "coffee" присвоить значения 3, 2, 1 соответственно, эти значения являются количеством
товара в одной упаковке. 
Создайте три переменных, которые содержат цены товара за одну штуку. 
Посчитайте сумму всех товаров и сохраните в переменной sum.
"""
# amount_milk = int(input('Введите количество молока:'))
# amount_chocolate = int(input('Введите количество шоколада:'))
# amount_coffee = int(input('Введите количество кофе:'))
# price_milk = int(input('Введите цену молока:'))
# price_chocolate = int(input('Введите цену шоколада:'))
# price_coffee = int(input('Введите цену кофе:'))
# sum = (amount_milk*price_milk+amount_chocolate*price_chocolate+amount_coffee*price_coffee)
# print('Итого:',sum)

"""Приветствие по вводу имени пользователя"""
# name = input('Введите свое имя:')
# greeting = "Привет, " + name
# print(greeting)

"""
Создайте 2 переменные со значениями 45 и 6, проверить делится ли
первое число на второе, если делится вывести соответствующее сообщение.
"""
# a=45
# b=46
# if 45/6:
#     print('Делится')

"""
Написать программу где надо ввести любой год и вывести сообщение
"Текущий год" если это текущий год, если будущий год вывести "Год еще не наступил" иначе "Год прошел".
"""
# year=int(input('Введите любой год:'))
# if year==2023:
#     print('Текущий год')
# elif year>2023:
#     print('Год еще не наступил')
# else:
#     print('Год прошел')

"""
Напишите код где где после ввода числа, на экран выводится делиться оно на 6 или нет.
"""
#Вариант 1
# num1=int(input('введите делимое'))
# num2=int(input('введите делитель'))
# if num1 % num2 == 0:
#     print('Делится')
# else:
#     print('Не делится')

#Вариант 2
# num1=int(input('Введите число:'))
# num2=6
# if num1 % num2==0:
#     print('Число делится на 6')
# else:
#     print('Число не делится на 6')

"""
Пользователь вводит три числа. Если все числа больше 10, то вывести на экран "yes", иначе "no"
"""
# num1=int(input('Введите число1:'))
# num2=int(input('Введите число2:'))
# num3=int(input('Введите число3:'))
# if num1>10 or num2>10 or num3 >10:
#     print('Yes')
# else:
#     print('No')

# ----------------
# a = input("vvedite gorod ")
# b = input("vvedite gorod ")
# c = input("vvedite gorod ")

# count_a = len(a)
# print(count_a)

# count_b = len(b)
# count_c = len(c)

# if count_a > count_b and count_a > count_c:
#     print(f'Bolshe {a}')
# elif count_b > count_a and count_b > count_c:
#     print(f'Bolshe {b}')
# elif count_c > count_a and count_c > count_b:
#     print(f'Bolshe {c}')

"""
Напишите программу, которая сравнивает пароль и его подтверждение.
Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
"""
# a=int(input('Введите логин:'))
# b=int(input('Введите пароль:'))
# if a==b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

"""
Спросить у пользователя его возраст, если значение больше или равно 18 вывести сообщение
"Совершеннолетний", если меньше или равно 4 вывести "Ребенок" иначе "Несовершеннолетий"
Если значение меньше 0 и больше 120 вывести сообщение "Недопустимый возраст!
"""
# age=int(input('Введите ваш возраст:'))
# if age<0 or age>120:
#     print('Недопустимый возраст')
# elif age <=4:
#     print('Ребенок')
# elif age>=18:
#     print('Совершеннолетний')
# else:
#     print('Несовершеннолетний')

"""
Напишите программу, которая определяет, разрешен ли пользователю доступ к интернет-ресурсу или нет.
Программа должна вывести текст «Доступ разрешен», если возраст не менее 18,' и «Доступ запрещен» - в противном случае.
"""
# age=int(input('Введите ваш возраст'))
# if age>=18:
#     print ('Доступ разрешен')
# else:
#     print ('Доступ запрещен')

"""
Запросить у пользователя ввести любое число и если это число больше 0
вывести сообщение "Положительное число", если меньше 0 вывести
сообщение "Отрицательное число" иначе вывести само число.
"""
# num=int(input('Введите число:'))
# if num>0:
#     print('Положительное число')
# elif num<0:
#     print('Отрицательное число')
# else:
#     print(num)

"""
Создайте условие которое определит самое большое и самое маленькое число из трёх.
"""
# a=int(input('Введите число1:'))
# b=int(input('Введите число2:'))
# c=int(input('Введите число3:'))
# print('Максимальным числом является:')
# if b<=a>=c:
#     print(a)
# elif a<=b>=c:
#     print(b)
# elif a<=c>=b:
#     print(c)
# print('Минимальным числом является:')
# if b>=a<=c:
#     print(a)
# elif a>=b<=c:
#     print(b)
# elif a>=c<=b:
#     print(c)

"""
Вывести числа от 1 до 10.(решить с помощью while и for)
"""
# for i in range (1,11):
#     print(i)
# #//////////////////////
# number = 1
# while number <= 10:
#     print(number)
#     number += 1

# name = ('Андрей','Петя','Ирина','Вася')
# for name in name:
#     print('Привет,'+ name +'!')

"""
Вывести все четные числа от 1 до 20. (решить с помощью while и for)
"""
# for number in range (1, 20 + 1):
#     if not number % 2:
#         print(number)
# ///////////////////////
# i = 0
# while i < 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

"""
Есть числа от 1 до 100. Если результат деления числа на 3 четная, то
вывести само число и результат от деления на 3.(решить с помощью while и for).
"""
# a=1
# b=100
# for i in range (a,b):
#     num = i / 3
#     c = i /3
#     if num % 2==0:
#         print(i, c)

# a=1
# while num <= 100:
#     if num % 3 == 0 and num % 2 == 0:
#         print(num,num//3)
#     a += 1

"""
Найти числа кратные 3 и 5 в диапазоне (1, 100).(решить с помощью while и for).
"""
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# i = 1
# while i <= 100:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1
# //////////////////////

"""
Напишите программу, которая выводит чётные числа из диапазона (1, 300) и останавливается, если встречает число 237.
"""
# for number in range (1, 300):
#     if number % 2 == 0:
#         print(number)
#         if number == 238:
#             break

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours,':',minutes,':',seconds)


# num = int(input("vedite chislo"))
# spisok_slov = []
# for _ in range(num):
#     text = input("Vvedite text ")
#     spisok_slov.append(text)
# print(spisok_slov)


"""
Напишите программу, которая считывает три целых числа  и выводит на экран их сумму. 
Каждое число записано в отдельной строке.
"""
# a=int(input('Input number:'))
# a+=int(input('Input number:'))
# a+=int(input('Input number:'))
# print('Sum of three numbers:',a)

# for i in range(1, 6, 2):
#     print(i)

# word = "Hello World!"
# for i in word:
#     if i == "l":
#         print("yes")

"""
Создайте переменную с именем number и присвойте ей значение 2.
Возведите число в куб и выведите его на экран.
"""
# number=2
# print(number**3)

"""
Выполните деление числа 1467 на 6 с округлением результата.
Для этого создайте переменную с любым именем, в неё запишите
нужное математическое действие и выведите переменную на экран.
Важно: используйте лишь один специальный оператор для выполнения этого действия.
"""
# number=1467//6
# print('Результат:',number)

"""
Создайте строку со значением: «Data».
Во вторую переменную запишите умножение строки на число 4.
Результат выведите на экран, должно получиться: «DataDataDataData».
"""
# string='Data\n'
# mult=string*4
# print(string*4)

# string='Data '
# mult=string*4
# print(string*4)

"""
Создайте список с именем lis. Поместите в него следующие элементы: 255, 5, 8, -4.5, 10.
Элементы нужно добавить при создании списка. 
Выведите на экран третий по номеру элемент.
"""
# lis = [255,5,8,-4.5,10]
# print(lis[2])

"""
У вас есть следующий список:
255, 5, 8, -4.5, 10.
Выведите на экран предпоследний элемент списка. 
Используйте для этого отрицательный индекс.
"""
# lis = [255,5,8,-4.5,10]
# print(lis[-2])

"""
Создайте список под названием «lis» и добавьте в него следующие элементы:
255, 5, 8, -4.5, 10, 9, 0, -0.2, 52.
При помощи срезов в Python выведите каждый второй элемент начиная со 2 элемента и по 6 элемент.
"""
# lis=[255,5,8,-4.5,10,9,0,-0.2,52]
# print(lis[1:5:2])

"""
Создайте переменную со значением 8.
При помощи сокращенной математической операции добавьте к ней число 12.
Выведите переменную на экран.
"""
# digit=8
# digit+=12
# print(digit)

"""
Создайте переменную с названием userName и присвойте ей значение «Bot».
Пропиши условие используя конструкцию if.
В условии проверьте является ли значение переменной равным значению «Bot». 
Если это будет так, то выведите на экран сообщение: «User is bot».
"""
# userName="bot"
# if userName == "bot":
#     print('User is bot')
"""
Напишите программу, которая считывает целое число,
после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
"""
# a = int(input('Введите число: '))
# print('Предыдущее число', a, 'это', a-1)
# print('Следущее число', a, 'это', a+1)

"""
Напишите программу, которая считывает целое положительное число xx и выводит 
на экран последовательность чисел x, 2x, 3x, 4x, 5x, разделённых тремя черточками.
"""
# x = int(input('Введите любое число: '))
# print(x, x*2, x*3, x*4, sep='-'*3)

"""
Напишите программу, которая находит полное число метров по заданному числу сантиметров.
"""
# a=int(input('Введите сантиметры: '))
# b=100
# print('Расстояние в метрах:', a/100)

"""
Напишите программу для пересчёта величины временного интервала, заданного в минутах,
в величину, выраженную в часах и минутах.
"""
# a=int(input('Введите время в минутах:'))
# print(a,'мин - это', a//60,'час(ов)', a % 60,'минут')

'-----------Использование f(format)-----------'
# #Пример без f
# name = "Jack"
# surname = "Jonathan"
# print(surname,''+name)
# #то же самое, только с f
# name = 'Jack'
# print(f'Jonathan {name}')
# #теперь при помощи просто f
# name = 'Jack'
# print('Jonathan {}'.format(name))

"""
Напишите программу, которая определяет, является число четным или нечетным.
"""
# a=int(input('Введите число: '))
# if a % 2:
#     print('Число нечетное')
# else:
#     print('Число четное')

'------APPEND------------------'
"""
append() добавляет в конец списка элемент, переданный ему в 
качестве аргумента. Как и все методы в Python, он вызывается через оператор . (точка).
"""
# a=['car','home','dog']
# a.append('cat')
# print(a)

"""
Усложним задачу и попробуем  добавить ещё один список из двух строк:
"""
# a=['car','home','dog']
# b=['moon','planet']
# a.append(b)
# print(a)
#ПРИМЕЧАНИЕ: чтобы элементы из b добавились отдельно? 
#К сожалению, с помощью append() этого сделать нельзя, потому что метод принимает только один аргумент. 
#ТО ДЛЯ ЭТОГО СУЩЕСТВУЕТ МЕТОД EXTEND(ниже)
#extend() принимает в качестве параметра итерируемый объект и объединяет его со списком.
# a=['car','home','dog']
# b=['moon','planet']
# a.extend(b)
# print(a)
"""
Чтобы упростить жизнь питонистам, разработчики языка добавили пару фич,
которые помогают быстро добавлять элементы в списки.
Оператор +. Он напоминает обычный математический оператор, но со списками действует как функция extend():
"""
# a=[1,2,3]
# b=[4,5,6]
# a+=b
# print(a)
"""
Напишите программу, которая определяет, является ли год с данным номером високосным. 
"""
# a=int(input('Введите год: '))
# if a % 4 == 0 or a % 400 == 0 or a % 100 == 0:
#     print(a,'год является высокосным')
# else:
#     print(a,'год не является высокосным')
"""
Написание числа в обратном порядке
"""
# number=int(input('Введите любое число: '))
# number =str(number)[::-1]
# print('Число в обратном порядке:',number)

'------------Работа со строками----------'
# s='Эта строка длинная'
# print(len(s)) #len - считает длину строки(т.е колво символов)

# s='Эта строка длинная'
# print(s.count('о')) # .count - считает кол-во повторяющихся символов

# s='Эта строка длинная'
# print(s.split('а')) #убирает указанный символ из строки

# lis=[255,5,-4.5,10] #элементы записываются в кважратны скобки
# print(lis[3]) #вывод элемента из списка производится путем создания кв.скобок и с указанием переменной в которой содержится элемент

# lis = [255, 5, 8, -4.5, 10]
# print(lis[-1]) #при выводе последнего элемента используется отрицательный индекс

'------------Срезы-------------'
'''
Создайте список под названием «lis» и добавьте в него следующие элементы:
255, 5, 8, -4.5, 10, 9, 0, -0.2, 52.
При помощи срезов в Python выведите каждый второй элемент начиная со 2 элемента и по 6 элемент.
'''
# lis=[255, 5, 8, -4.5, 10, 9, 0, -0.2, 52]
# print(lis[1:8:2]) #c 1 по 8 это срез, а последнее число это шаг

'''
Создайте переменную со значением 8. При помощи сокращенной математической операции добавьте к ней число 12.
Выведите переменную на экран.
'''
#Вариант1
# num=8
# print(num+12)

#Вариант2(при помощи сокращенной математической операции)
# digit = 8
# digit += 12
# print(digit)

#Вариант3(со словами)
# string1 = 'Hello'
# string1 += ' World!'
# print(string1)

