a = input('Enter the value ')
b = input('Enter the value ')
c = input('Enter the value ')
if a == b == c:
    print("3")
elif a == b or b == c or c == a:
    print('2')
else:
    print('0')
