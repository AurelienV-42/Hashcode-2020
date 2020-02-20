#!/usr/bin/env python3

import sys

B = 0
L = 0
D = 0


def parse(path_to_file):
    global B, L, D
    file = open(path_to_file, "r")
    content = file.read()
    i = 0
    splitted = content.split('\n')
    for line in splitted:
        numbers = line.split(' ')
        if i == 0:
            B = int(numbers[0])
            L = int(numbers[1])
            D = int(numbers[2])
        i += 1
    return content


def main():
    print(parse(sys.argv[1]))
    print(B, L, D)


if __name__ == "__main__":
    main()
