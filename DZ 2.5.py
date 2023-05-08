month = int(input('Input number from 1 to 12: '))
print({
    1:'January, Winter',
    2:'Fabruary, Winter',
    3:'March, Spring',
    4:'April, Spring',
    5:'May, Spring',
    6:'June, Summer',
    7:'July, Summer',
    8:'August, Summer',
    9:'September, Autumn',
    10:'October, Autumn',
    11:'November, Autumn',
    12:'December, Winter'
}.get(month,'Invalid number'))