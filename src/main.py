#!/usr/bin/env python3

import sys

# Input
B = 0
L = 0
D = 0
S = []
LIBRARY = []

# Output
NB_LIBRARY = 0
WHICH_LIBRARY = []


def lib_ratio(lib):
    lib["R"] = lib["N"] / lib["M"] + lib["T"]


def parse(path_to_file):
    global B, L, D, S, LIBRARY
    file = open(path_to_file, "r")
    content = file.read()
    i = 0
    splitted = content.split('\n')
    new_library = {"N": 0, "T": 0, "M": 0, "IDS": []}
    for line in splitted:
        numbers = line.split(' ')
        if len(numbers) == 1:
            return content
        elif i == 0:
            B = int(numbers[0])
            L = int(numbers[1])
            D = int(numbers[2])
        elif i == 1:
            for tmp in numbers:
                S += tmp
        elif i % 2 == 0:
            new_library["N"] = int(numbers[0])
            new_library["T"] = int(numbers[1])
            new_library["M"] = int(numbers[2])
            new_library["IDS"] = []
        else:
            for tmp in numbers:
                new_library["IDS"] += tmp
            LIBRARY += new_library.copy(),
        i += 1
    return content


def main():
    parse(sys.argv[1])
    for Lib in LIBRARY:
        lib_ratio(Lib)
    print(B, L, D)
    print(S)
    print(LIBRARY)

    library_process = {"Idx": 0, "T": 0, "M": 0, "IDS": []}

    print(NB_LIBRARY)
    for tmp in WHICH_LIBRARY:
        print(tmp)

if __name__ == "__main__":
    main()
