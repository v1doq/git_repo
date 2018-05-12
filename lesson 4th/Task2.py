def pre_max_value(*numbers):
    values = list(numbers)
    values = sorted(values)
    n = -1
    while True:
        if values[-1] == values[n]:
            n = n - 1
        else:
            return values[n]


print(pre_max_value(8, 3, 8, 5, 5, 6, 7, 6, 6))
