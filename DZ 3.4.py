a = float(input('First managaer: '))
if a < 500:
    a = ((a*3/100)+200)
elif a >= 500 and a <= 1000:
    a = ((a*5/100)+200)
elif a > 1000:
    a = ((a*8/100)+200)
b = float(input('Second Manager: '))
if b < 500:
    b = ((b*3/100)+200)
elif b >= 500 and b <= 1000:
    b = ((b*5/100)+200)
elif b > 1000:
    b = ((b*8/100)+200)
c = float(input('Third manager: '))
if c < 500:
    c = ((c*3/100)+200)
elif c >= 500 and c <= 1000:
    c = ((c*5/100)+200)
elif c > 1000:
    c = ((c*8/100)+200)
print('First manager - ',a)
print('Second manager - ',b)
print('Third manager - ',c)
print('Best manager\'s salary',max(a,b,c)+200,)
