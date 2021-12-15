import random

x = set([random.randint(0, 10) for _ in range(10)])
y = set([random.randint(0, 10) for _ in range(13)])

print(x)
print(y)

a = len(x) + len(y) - len(x & y)

print(a)