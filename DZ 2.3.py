a = int(input('Metres: '))
print('1 - miles')
print('2 - inches')
print('3 - yards')
choose = int(input('Make a choice: '))
if choose == 1:
    print(a*0.0006)
elif choose == 2:
    print(a*39.37)
elif choose == 3:
    print(a*1.093)
else:
    print('Invalid choice')