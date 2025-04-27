#!/usr/bin/python3

"""
Minimum Operations

"""


def minOperations(n):
    if n < 2:
        return 0

    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += i
            n = n // i
        i += 1
    return operations
