import random

lst = [random.randint(0,100) for _ in range(10)]

print(lst)

k = int(input("Enter an index: "))

lst.remove(lst[k])
lst.pop(-1)

print(lst)