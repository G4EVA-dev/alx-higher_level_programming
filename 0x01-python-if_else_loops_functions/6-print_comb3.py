#!/usr/bin/python3
for w in range(0, 10):
    for z in range(w + 1, 10):
        if w == 8 and z == 9:
            print('89')
        else:
            print('{}{}, '.format(w, z), end='')
