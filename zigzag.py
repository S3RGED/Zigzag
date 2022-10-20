#!/usr/bin/env python3
from time import sleep


def zigzag(threshold, width, delay):
    irange = threshold
    for i in range(irange):
        print(' ' * threshold + '*' * width)
        sleep(delay)
        threshold -= 1

    for i in range(irange):
        print(' ' * threshold + '*' * width)
        threshold += 1
        sleep(delay)


try:
    for i in range (10):
        zigzag(h, 5, 0.03)
except NameError:
    print('Wrong value')
