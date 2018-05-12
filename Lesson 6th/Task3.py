my_source = open("source.txt", "r", encoding='UTF-8')
my_destination = open("destination.txt", "w")
my_source = str(my_source.read())
my_source = my_source.split(" ")
for i in range(len(my_source)):
    my_source[i] = my_source[i].strip('.!()')
my_source.sort(key=str.lower)
n = 0
for i in my_source:
    i = my_source[n]
    print(i, file=my_destination)
    n += 1
print(my_source)
