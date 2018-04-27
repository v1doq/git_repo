def is_year_leap(a):
    """Current function checks if the year is High year or Low year"""
    if ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)):
        return True
    else:
        return False


def triangles(a, b, c):
    """Current function checks if triangle with these values could be or not"""

    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

'''
result = is_year_leap(int(input('Enter a year ')))
print(result)

a = int(input('Enter first side of the triangle '))
b = int(input('Enter second side of the triangle '))
c = int(input('Enter third side of the triangle '))
result = triangles(a, b, c)
print(result)
'''