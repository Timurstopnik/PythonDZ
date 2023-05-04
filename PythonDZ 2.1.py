a=int(input('Number1: '))
b=int(input('Number2: '))
c=int(input('Number3: '))
print('1: summ')
print('2: mult')
choose = int(input('Choose action'))
if choose == 1:
    print(a+b+c)
elif choose == 2:
    print(a*b*c)
else:
    print('Invalid choice')