def word():
    while True:
        new_string = input('Enter Word')
        if " " not in new_string.strip():
            break
    return new_string


def enter_number():
    while True:
        number = input('Enter number')

        if number.isdigit():
            break
    number = int(number)
    return number


print(word())
print(enter_number())
