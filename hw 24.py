'''

ДЗ 24. Написать функцию season
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года (в виде строки),
которому этот месяц принадлежит (зима, весна, лето или осень).

'''

def season(month):
    if 0 < month < 3 or month > 11:
        x = 'Winter'
    elif 2 < month < 6:
        x = 'Spring'
    elif 5 < month < 9:
        x = 'Summer'
    else:
        x = 'Autumn'

    return x

print(season(1))
print(season(2))
print(season(3))
print(season(4))
print(season(5))
print(season(6))
print(season(7))
print(season(8))
print(season(9))
print(season(10))
print(season(11))
print(season(12))