a = int(input('Input number: '))
print('1 - first degree')
print('2 - second degree')
print('3 - Third degree')
print('4 - fourth degree')
print('5 - fifth degree')
print('6 -  sixth degree')
print('7 - seventh degree')
b = int(input('Choose a degree: '))
if b == 1:
    print(a**1)
elif b == 2:
    print(a**2)
elif b == 3:
    print(a**3)
elif b == 4:
    print(a**4)
elif b == 5:
    print(a**5)
elif b == 6:
    print(a**6)
elif b == 7:
    print(a**7)
else:
    print('error')