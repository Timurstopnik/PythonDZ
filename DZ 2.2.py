a = int(input('number 1: '))
b = int(input('Number 2: '))
c = int(input('Number 3: '))
print('1 - Highest number')
print('2 - Lowest number')
print('3 - Average')
choice = int(input('choose action: '))
if choice == 1:
    print(max(a,b,c))
elif choice == 2:
    print(min(a,b,c))
elif choice == 3:
    print(a+b+c/3)
else :
    print('Invalid choice')