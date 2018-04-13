number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
while int(len(number_list) > 0):
    print(number_list)
    number_list.pop(0)
print(len(number_list))#Проверка что лист пустой

new_string = "Helloworld"
#new_string = input()
for i in range(len(new_string)):
    print(new_string)
    new_string = new_string[1:]
print(len(new_string))#Проверка что строка пуска
