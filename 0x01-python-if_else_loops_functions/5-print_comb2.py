#!/usr/bin/python3
for dosnumeros in range(0, 100):
    if dosnumeros == 99:
        print("{}".format(dosnumeros))
    else:
        print("{:02}".format(dosnumeros), end=", ")
