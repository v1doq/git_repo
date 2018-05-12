string = input('Enter string')
s = str(string)
sep = int(len(string) / 2)
end = int(len(string))
if (len(string)) % 2 == 0:
    string = string[sep: end] + string[0:sep]
    print(string)
else:
    string = string[sep + 1: end] + string[0:sep + 1]
    print(string)
