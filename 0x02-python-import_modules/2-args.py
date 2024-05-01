#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
if count == 1:
    print("{} argument:".format(count))
elif count == 0:
    print("{} arguments.".format(count))
else:
    print("{} arguments:".format(count))
for i in range(1, count + 1):
    print(f"{i}: {sys.argv[i]}")
