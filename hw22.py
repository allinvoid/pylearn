'''

ДЗ 22. Написать функцию is_year_leap
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True, если год високосный, и False иначе.
Дополнительно здесь: Григорианский календарь

'''

def is_year_leap(year):
    if year % 4 == 0 or (year % 100 == 0  and year % 400 != 0):
        return False
    else:
        return True

print(is_year_leap(1100))
print(is_year_leap(1834))