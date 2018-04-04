# Task 1
string = input()
print(string.isdigit())
# Task 2
string = input()
number = string.count('.')
print(number)
# Task 3
string = input()
number = string.count(' ')
print(number)
# Task 4
string = 'HomeWork'
string = string.center(100)
print(string)
print(len(string))
# Task 5
string = input()
print(string.title())

# Task1
import math
a = 179
b = 971
c = a**2 + b**2
print(math.sqrt(c))

# Task2
number = int(input('Enter value '))
number = number //10
print(number)
# Task3
number = int(input('Enter value '))
number = str(number)
n1 = int(number[0])
n2 = int(number[1])
n3 = int(number[2])
summ = n1+n2+n3
print(summ)
# Task4
number = int(input('Enter value '))
if number % 2 == 0:
    print(number+2)
else:
    print(number+1)
# Task5
number = float(input('Enter value'))
print(str(number % 1)[2:])
# Task6
number = float(input('Enter value'))
print(str(number % 1)[2:])
#####################################

a = input('Enter the value ')
b = input('Enter the value ')
c = input('Enter the value ')
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')
#################################
    s[0] = input('Enter the value ')
    b = str(input('Enter the value '))
    c = str(input('Enter the value '))
    s = [a, b, c]
    print(s.sort())
    ##########################
a = input('Enter the value ')
b = input('Enter the value ')
c = input('Enter the value ')
if a = b = c:
