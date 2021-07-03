def min():
    a=input('enter 1st number')
    b=input('enter 2nd number')
    c=input('enter 3rd number')

    if a<b and b<c:
        print('a is the smallest')
    elif b<c:
        print('b is the smallest')
    else:
        print('c is the smsllest')
min()