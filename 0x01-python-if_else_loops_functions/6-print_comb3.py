#!/usr/bin/python3
for combination in range(0, 10):
    for combination2 in range(combination + 1, 10):
        if combination == 8 and combination2 == 9:
            print("{}{}".format(combination, combination2))
        else:
            print("{}{}".format(combination, combination2), end=", ")
