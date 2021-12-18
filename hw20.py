'''

ДЗ 20. Задача на словари 2
Дан текст (много строк в одном вводе) состоящий из нескольких строки.
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.

'''


x = input("String: ")

x1 = x.split(' ')

dct = {}
dct = dct.fromkeys(x1)

for key, value in dct.items():
    dct[key] = x1.count(key)

maxi = max(dct.values())
a = ''

for key, value in dct.items():
    if value == maxi:
        a = key

print(a)