'''

Hаписать функцию, принимающую ТРИ параметра и выполняющая циклически сдвиг целого числа (первый параметр)
на N разрядов (второй параметр) вправо или влево, в зависимости от значения третьего параметра функции.
Третий параметр булевский, задаёт направление сдвига (по умолчанию влево (False)).

'''



def sdwig(numb, n, side=False):
    x = 1
    if side:
        for _ in range(n):
            x *= 10
    else:
        for _ in range(n):
            x /= 10

    x *= numb
    return x

print(sdwig(1234, 5))