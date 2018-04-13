new_string = "We are not what we should be! We are not we need to be. But at least we are not what we used to be (Football Coach)"
new_string = new_string.split(' ')
for i in range(len(new_string)):
    new_string[i] = new_string[i].strip('.!()')
print(len(new_string))
new_string.sort(key=str.lower)
print(new_string)

'''a = dict.fromkeys(new_string)
print(len(a))'''