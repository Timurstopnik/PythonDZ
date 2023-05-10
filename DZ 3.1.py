a = int(input('Input number from 1 to 100: '))
c = 3
b = 5
if a < 1 or a > 100:
    print('Error')
elif a % c == 0 and a % b == 0:
    print('Fizz Buzz')
elif a % c == 0:
    print('Fizz')
elif a % b == 0:
    print('Buzz')
elif a % c != 0 or a % b != 0:
    print(a)
