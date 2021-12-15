s = input("Строка: ");

third = s[2];
prelast = s[-2];
first_five = s[: 5];
bez3 = s[: -2];
chetid = s[0: : 2];
nechetid = s[1: : 2];
swap = s[: : -1];
sp2swap = ' '.join(swap);


print(third);
print(prelast);
print(first_five);
print(bez3);
print(chetid);
print(nechetid);
print(swap);
print(sp2swap);
print(len(s));