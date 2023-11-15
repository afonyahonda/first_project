"--------КОНКАТЕНАЦИЯ-------"
#Конкатенация в Python это метод соединения строк.

#ВАРИАНТ 1
# str1 = 'Hello '
# str2 = 'World'
# str3 = str1 + str2
# print(str3)

#ВАРИАНТ 2 через .join
# str = ['Hello','World']
# str2 = ' '.join(str)
# print(str2)

#ВАРИАНТ 2(1) через .join
# str = ['Ich','Liebe','Python']
# result = ' '.join(str)
# print(result)

#ВАРИАНТ 3 через .join
# first_name = 'Heinrich'
# last_name = 'Himmler'
# str = ['Meine name ist', first_name, last_name]
# result = ' '.join(str)
# print(result)

'--------КОНКАТЕНАЦИЯ СТРОК И ЧИСЕЛ------'
#ОШИБКА
# age = 28
# message = 'Ich bin ' + age + ' jahre alt'
#В данном случае код вызовет ошибку TypeError, 
# потому что мы пытаемся соединить строку с числом без преобразования числа также в строку.

#ПРАВИЛЬНО
# age = 28
# message = "Ich bin " + str(age) + " jahre alt."
# print(message)
#Мы преобразовали число, заключенное в переменную age, в строку с помощью 
#функции str(),и интерпретатор выдал нам нужный результат.

#ЧЕРЕЗ МЕТОД format
# age = 28
# message = 'Ich bin {} jahre alt.'.format(age)
# print(message)

#Конкатенация строки и числа через f-строки
# age = 28
# message = f'Ich bin {age} jahre alt.'
# print(message)

# name = 'Izolda'
# age = 28
# print(f'Meine name ist {name} und Ich bin {age} jahre alt.')

'-------------ЗАДАНИЯ---------'
"""
Запросить у пользователя две строки, Создать предложение где одна
его половина написана в маленьком регистре, а вторая полностью в
большом.
"""
# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# print(name.lower(), surname.upper())

"""
Попросить пользователя ввести текст состоящий только из букв.
Если в тексте присутствуют символы кроме букв, то вывести
сообщение "Ввести только буквы", если всё верно вывести
введенный текст в нижнем регистре.
"""
# def validate_text(text):
#     for char in text:
#         if not char.isalpha():
#             return False
#         return True
# def main():
#     text = input('Введите текст только из букв: ')
#     if validate_text(text):
#         print(text.lower())
#     else:
#         print('Ввести только буквы')
# main() 
