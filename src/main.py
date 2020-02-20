#!/usr/bin/env python3

import sys
from math import ceil

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
    lib["R"] = ceil(lib["N"] / lib["M"] + lib["T"])


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


def output():
    global NB_LIBRARY, WHICH_LIBRARY
    print(NB_LIBRARY)
    for tmp in WHICH_LIBRARY:
        print(tmp["Idx"], tmp["Nb_books"])
        for i in tmp["Idx_book"]:
            print(i, end=' ')


def algorithm():
    global B, L, D, S, LIBRARY, NB_LIBRARY, WHICH_LIBRARY
    for Lib in LIBRARY:
        lib_ratio(Lib)
    library_process = {"Idx": 0, "Nb_books": 0, "Idx_book": [3, 4, 2]}
    WHICH_LIBRARY += library_process,


def main():
    parse(sys.argv[1])
    algorithm()
    output()


if __name__ == "__main__":
    main()
