a = input('Enter the value ')
if ((a%4 == 0 and a%100 != 0) or (a%400 == 0)):
    print('High year')
else:
    print('Low year')