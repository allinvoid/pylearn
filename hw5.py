first = int(input("Количество учеников А: "));
second = int(input("Количество учеников Б: "));
third = int(input("Количество учеников В: "));

students = first + second + third;

tables = students // 2;
tables += students % 2;

print(tables);