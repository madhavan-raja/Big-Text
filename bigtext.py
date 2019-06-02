from characters_3w import Palette


def display(msg, hor_scale=1, ver_scale=1, space_char=' ', true_char='█', false_char=' '):
    char_height = Palette.height

    for h in range(char_height):
        for x in range(ver_scale):
            for ch in msg:
                for line in Palette.chars.get(ch)[h]:
                    for big_chr in line:
                        for y in range(hor_scale):
                            if big_chr == ' ' or big_chr == '0':
                                print(false_char, end='')
                            else:
                                print(true_char, end='')
                print(space_char, end='')
            print()
