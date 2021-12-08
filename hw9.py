i = 1;
cnt = 0;
suma = 0;
sred = 0;
pred = 0;
maxi = 0;
mini = 0;
chet = 0;
nechet = 0;

while True:

	i = int(input("Число: "));
	
	if i == 0:
		break;
	
	if not i % 2:
		chet += 1;
		
	if i % 2:
		nechet += 1;
	
	cnt += 1;
		
	suma += i;
	sred = suma / cnt;
	
	if cnt == 1:
		mini = i;
	
	if i < mini:
		mini = i;
	
	if i > pred:
		maxi = i;
		
	pred = i;
	
	

print("Сумма: ", suma);
print("Среднее арифм: ", sred);
print("Макс значение: ", maxi);
print("Мин значение: ", mini);
print("Кол-во четных: ", chet);
print("Кол-во нечетных: ", nechet);



	