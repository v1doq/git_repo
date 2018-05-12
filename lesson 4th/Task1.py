def lalala(a=3, b=3, c=0):
    item = 1
    song_string = 'la'
    while item < b:
        song_string += '-la'
        item += 1
    song_string = ('\n' + song_string) * a
    if c == 0:
        return song_string + '.'
    elif c == 1:
        return song_string + '!'


print(lalala(5, 5, 1))
