s = input("String with h: ");

first = s.find("h");
last = s.rfind("h");


a = s[ : first + 1];
b = s[first + 1 : last];
c = s[last : ];

rep = b.replace("h", "H");

print(a + rep + c);


