from characters_3w import *


def display(msg, hor_scale=1, ver_scale=1, space_char=' ', true_char='█', false_char=' ', absent_char='!'):
    for h in range(height):
        for x in range(ver_scale):
            for ch in msg:
                for line in chars.get(ch, [['!']] * height)[h]:
                    for big_chr in line:
                        for y in range(hor_scale):
                            if big_chr == '!':
                                print(absent_char, end='')
                            elif big_chr == ' ' or big_chr == '0':
                                print(false_char, end='')
                            else:
                                print(true_char, end='')
                print(space_char, end='')
            print()
