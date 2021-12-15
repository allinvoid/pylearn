s = input("String and chr: ");

a = s[-1];
start = 0;
k = len(s);
b = 0;

while True:
	b = s.find(a, start);
	
	start = b+1;
	
	if b == k -1:
		break;
		
	print(b);
	
