'''

ДЗ 23. Написать функцию square
Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

'''

def square(st):
    p = st * 4
    s = st ** 2
    d = (2 ** 0.5) * st
    res = {p, s, d}
    return res

print(square(8))
