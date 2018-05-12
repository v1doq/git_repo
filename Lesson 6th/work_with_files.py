new_file = open("Test_write.txt", "w")


my_file = open("Task1.txt", "r+")
my_file.write("Hello_world \n")

i = 1
for line in my_file:
    line = "Number: " +str(i)+" " + line.rstrip() + "!"
    print(line, file=new_file)
    i += 1
