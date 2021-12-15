x = input("String: ")

x1 = x.split(' ')

dct = {}
dct = dct.fromkeys(x1)

for key, value in dct.items():
    dct[key] = x1.count(key)

print(dct)