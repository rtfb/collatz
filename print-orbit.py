#!/usr/bin/env python3

import argparse
import sys

from random import randint


def collatz(num):
    orbit = []
    while num != 1:
        if num % 2 == 0:
            num = num >> 1
        else:
            num = num + (num << 1) + 1
        orbit.append(num)
    return orbit


def print_orbit(num):
    orbit = collatz(num)
    path_record = max(orbit + [num])
    print('length: {}, path record: {}'.format(len(orbit), path_record))
    for i in orbit:
        print(i, hex(i), bin(i))


def random_sample(nsamples):
    orbits = []
    for i in range(nsamples):
        num = randint(0, 0xffffffff)
        orbit = collatz(num)
        path_record = max(orbit + [num])
        orbits.append((num, len(orbit), path_record,))
    for oo in orbits:
        n, o, p = oo
        overflow = ''
        if p > 0xffffffff:
            overflow = '  #  << OVERFLOW'
        print('({}, {}, {}),{}'.format(n, o, p, overflow))


def run(args):
    if args.number is not None:
        return print_orbit(args.number)
    random_sample(args.nsamples)


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', '--random', help='random sample N orbits',
                       action='store', dest='nsamples', type=int)
    group.add_argument('-o', '--orbit', help='compute and print a single orbit',
                       action='store', dest='number', type=int)
    args = parser.parse_args()
    run(args)


if __name__ == '__main__':
    main()
