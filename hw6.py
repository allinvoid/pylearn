swap = int(input("Введите трехзначное положительное число: "));

x1 = swap // 100;
x2 = (swap // 10) % 10;
x3 = swap % 10;

print(x3, x2, x1, sep="");