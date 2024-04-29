#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    else:
        ans = 1
        for _ in range(b):
            ans *= a
    return ans
