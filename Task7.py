def triangle(a, b, c):
    """Current function checks if triangle with these values could be or not,
    Also it shows what type of the triangle it is"""

    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return ('It is a Equilateral triangle')

        if a != b and b != c and c != a:
            return ('It is a Versatile triangle')
        if a == b or b == c or c == a:
            return ('It is a Isosceles triangle')
    else:
        return ('It is not a triangle')

'''
a = input('Enter the value ')
b = input('Enter the value ')
c = input('Enter the value ')
result = triangle(a, b, c)
print(result)
'''