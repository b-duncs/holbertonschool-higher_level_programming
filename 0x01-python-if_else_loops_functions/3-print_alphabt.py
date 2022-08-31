#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) != 'q' and 'e' != chr(alpha):
        print("{}".format(chr(alpha)), end="")
