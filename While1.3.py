a = (int(input('a= ')))
b = int(input('b= '))
while a < b:
    a+=1
    if a % 3 == 0 and a % 5 == 0:
        print(a,'Fizz Buzz')
    elif a % 3 == 0:
        print(a,'Fizz')
    elif a % 5 == 0:
        print(a,'Buzz')
    else:
        print(a)