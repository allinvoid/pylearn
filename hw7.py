n = int(input("Граница вывода корня натурального числа: "));

s = 1;

for i in range(1, n):
	i **= 2;
	if i > n+1:
		break;
	print(i, end = " ");
	