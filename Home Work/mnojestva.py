'---------МНОЖЕСТВА--------'
#Множества в пайтон - это мешок содержащий неупорядоченные
#значения любых типов.

#Множества создаются с помощью фигурных '{}' скобок или set

# my_set = {1,2,3,4}

#С помощью функции set которая преобразует итерируемые объекты во множество.
# my_list = [6,7,8,9]
# my_set = set(my_list)
# print(my_set)

'------ЗАДАНИЯ---------'
"""
Исправьте ошибки в коде, чтобы получить требуемый вывод.
d1 = {"a": 100. "b": 200. "c":300}
d2 = {a: 300, b: 200, d:400}
print(d1["b"] == d2["b"])
требуемый вывод:
True
"""
# d1 = {"a": 100, "b": 200, "c": 300} #здесь ошибка в символах
# d2 = {"a": 300, "b": 200, "c": 400}
# print(d1["b"] == d2["b"])

"""
Выведите значение возраста из словаря person.
person = {"name": "Kelly", "age":25, "city": "New york"}
"""
# person = {"name": "Kelly", "age":25, "city": "New york"}
# age = person["age"] #используем ключ age для получения значения возраста
# print(age) #потом уже выводим значение возраста

"""
Напишите код который добавит все элементы списка в множество
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
"""
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)
#В этом примере мы используем метод 'update()' для множества
# sample_set, передавая ему список sample_list.
# Тем самым метод update() добавит все элементы списка во множество
# расширяя его. 

"""
Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент. А затем
удалите через .pop() элемент и посмотрите что же вы удалили.
"""
# my_set = {'USA', 'Mexica', 'Panama', 'India', 'Russia'}
# my_set.add('Canada')
# removed_element = my_set.pop()
# print(removed_element)
# print(my_set)
#В этом примере мы сначала создаем множество с 5 элементами
#Затем мы добавляем еще 1 элемент с помощью команды .add
#Затем удаляем элемент с помощью команды .pop сохраняя его значение в переменную
#removed.element
#Наконец мы выводим удаленный элемент и обновленное множество на экран

"""

"""
