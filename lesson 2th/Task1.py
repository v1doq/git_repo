string = input('Enter string')
try:
    print(string[2], string[-2], string[0:5], string[0:-2], string[0::2], string[1::2], string[::-1], string[::-2], string[-2:0:-1], len(string), sep='\n')
except IndexError as e:
    print(e)