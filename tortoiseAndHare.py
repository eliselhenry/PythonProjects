~# This program simulates a race between the tortoise and the hare using
# randomly generated integers.

import random

def TvsH():
    t_pos = 1
    h_pos = 1
    time = 0
    print('On Your Mark... ')
    print('Get Set...')
    print('GO!!!')
    print('And They\'re Off!')
    print()

    while t_pos < 50 and h_pos < 50:
        t_pos = tortoise(t_pos)
        h_pos = hare(h_pos)
        race(t_pos, h_pos)
        time += 1

    if t_pos == 50:
        print()
        print('Tortoise Wins!!')

    elif h_pos == 50:
        print()
        print('Hare Wins!!')

    print('It took', time, 'seconds to finish the race.')

def tortoise(pos):
    y = random.randint(1, 10)
    if y >= 1 and y <= 5:
        pos += 3
    elif y >= 6 and y <= 7:
        pos -= 5
    else:
        pos += 1
    if pos >= 50:
        pos = 50
    if pos <= 1:
        pos = 1
    return pos


def hare(pos):
    y = random.randint(1, 10)
    if y >= 1 and y <= 2:
        pos += 0
    elif y >= 3 and y <= 4:
        pos += 7
    elif y == 5:
        pos -= 10
    elif y >= 6 and y <= 8:
        pos += 1
    else:
        pos -= 2
    if pos >= 50:
        pos = 50
    if pos <= 1:
        pos = 1
    return pos


def race(t_pos, h_pos):
    if t_pos > h_pos:
        for x in range(h_pos):
            print(' ', end='')
        print("H", end='')
        for y in range(t_pos - h_pos):
            print(' ', end='')
        print('T')

    elif t_pos < h_pos:
        for x in range(t_pos):
            print(' ', end='')
        print("T", end='')
        for y in range(h_pos - t_pos):
            print(' ', end='')
        print('H')
    else:
        for y in range(t_pos):
            print(' ', end='')
        print("OW!")


TvsH()
