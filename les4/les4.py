n = input("Введите количество школьников: ");
k = input("Введите количество яблок: ");

a = int(k) // int(n);
b = int(k) % int(n);

print("Каждый школьник получил",a ,"яблок(а)");

if b == 0:
    print("Корзина пуста");
elif b != 0:
    print("В корзине осталось", b, "яблок(а)");