my_file = open("Task1.txt", "a")
my_file.write("Hello_world \n")
my_file.close()
my_second_file = open("Person.py", "r")
#print(my_second_file.read())
my_second_file.close()
new_file = open("Test_write.txt", "w")
my_file = open("Task1.txt", "r")
i = 1
for line in my_file:
    line = line.rstrip() + "!-"+str(i)
    print(line, file=new_file)
    i +=1
