myList = [64, 23, 834, 6, 143, 76]
len(myList)

#average
Sum = 0

for i in myList:
    Sum = Sum + i

a = (Sum / len(myList))
print('average: ')
print(a)

#variance
Sum = 0

for i in myList:
    Sum = Sum + ((i-a)**2)

b = (Sum / len(myList))
print('variance: ')
print(b)