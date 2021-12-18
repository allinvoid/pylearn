'''

ДЗ 21. Функция arithmetic
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Функция должна вернуть результат вычислений зависящий от третьего аргумент: + сложить их; - вычесть; * умножить; / разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".

'''

def arithmetic(a, b, op=0):
    if op == 0:
        print('Unknowing operation')
    else:
        x = op(a, b)
        return x

def ad(a, b):
    x = a + b
    return x

def mult(a, b):
    x = a * b
    return x

def subt(a, b):
    x = a - b
    return x

def div(a, b):
    x = a / b
    return x


print(arithmetic(3, 5, ad))
print(arithmetic(3, 5, mult))
print(arithmetic(3, 5, subt))
print(arithmetic(3, 5, div))
arithmetic(3, 5)
