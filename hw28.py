'''

Необходимо написать функцию которая разворачивает исходный список наоборот.
Алгоритм прост и ваши действия заключаются в следующем: мы меняем местами
0-ый элемент с последним, 1-ый с предпоследним и д.т. Итого количество таких
обменов будет равно половине длины списка. Иначе элементы поменяются местами
по-второму кругу и вернутся в первоначальное положение.
Применять функцию revers() или срезы с шагом -1 нельзя. Так же, нельзя использовать
дополнительные переменные (можно использовать переменную цикла for) или дополнительные списки.

'''

def obratka(lst):
    fin = len(lst) - 1
    i = 0

    while i <= fin // 2:
        lst[i], lst[fin] = lst[fin], lst[i]
        i += 1
        fin -= 1

    return lst

x = [1, 2, 3, 4, 5, 6, 7]
print(obratka(x))