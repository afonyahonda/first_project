'-----СЛОВАРИ-------'
#Словари в пайтон это данные с ключами и значениями.

# students_ages = dict(Amanda = 27, Nikol = 25, Alex = 22)
# print(students_ages)

#методы можно комбинировать
# students_ages = dict({'Amanda': 27, 'Nikol': 25, 'Alex':22}, Paul = 17, Maria = 21)
# print(students_ages)

# students_ages = ([('Amanda',27), ('Nikol,25'), ('Alex,22')])
# print(students_ages)

#создание словаря с исполльзванием двух списков и с помощью итератора zip
# students = ['Amanda', 'Nikol', 'Alex']
# ages = [27, 25, 22]
# students_ages = dict(zip(students, ages))
# print(students_ages)

#pop удаляет один элемент
# country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# country.pop('name')
# print(country)

#popitem удаляет (по элементу) последний элемент
# country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# country.popitem()
# country.popitem() #если повторно запустить то предпоследний элемент будет удален
# print(country)

#команда для отображениия только ключей
# country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# print(country.keys())

#команда для отображениия только значений
# country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# print(country.values())

#команда для отображениия ключей и значений
# country = {'code': 'RU', 'name': 'Russia', 'population': 144}
# print(country.items())

# person = {
#     'user1':{
#         'name': 'Petya',
#         'surname': 'Ivanov',
#         'age': 45,
#         'adress':('Moscow', 'Novaya str', '66'),
#         'grades': {'math':5, 'history':3, 'biology':4}

#     }
# }
# print(person['user1']['grades'])

#подсчет кол-ва повторяющихся символов
# s=input()
# d = {}
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# print(d)

#установка соответствия между объектами
# words=()
# while True:
#     s = input()
#     if s in words:
#         print('Слово', s, 'переводится как', words[s])
#     else:
#         print('Введите перевод слова', s)
#         translate = input()
#         words[s] = translate