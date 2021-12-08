n = int(input("Не превосходит: "));

s = 2;
i = 1;
a = 0;

while True:
	
	if s < n:
		a = s;
		
	if s > n:
		break;
		
	s *= 2;
	i += 1;
	
print(a, i);



