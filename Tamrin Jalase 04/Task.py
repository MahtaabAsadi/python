x1 = int(input('number 01: '))
x2 = int(input('number 02: '))
x3 = int(input('number 03: '))

if x1<x2:
    y1 = x1
    y2 = x2
else:
    y1 = x2
    y2 = x1    

if y1<x3:
    y1 = x1
else:
    y1 = x3

if y2>x3:
    y2 = x2
else:
    y2=x3

print(y1)
print(y2)
