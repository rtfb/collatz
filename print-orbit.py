#!/usr/bin/env python3

import sys


def collatz(num):
    orbit = []
    while num != 1:
        if num % 2 == 0:
            num = num >> 1
        else:
            num = num + (num << 1) + 1
        orbit.append(num)
    return orbit


def main():
    if len(sys.argv) < 2:
        print('usage: print-orbit.py [number]')
        return
    arg = sys.argv[1]
    try:
        num = int(arg)
    except ValueError:
        print('failed to parse the given argument "{}" as integer'.format(arg))
        return
    orbit = collatz(num)
    print('length: ', len(orbit))
    for i in orbit:
        print(i, hex(i), bin(i))


if __name__ == '__main__':
    main()
