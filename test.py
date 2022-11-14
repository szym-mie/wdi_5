from math import isqrt
from random import randint


N = 10
T = [2, 3, 6, 7]


def is_prime(n):
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    d = 5
    while d <= isqrt(n):
        if n % d == 0:
            return False

        d += 2

        if n % d == 0:
            return False

        d += 4

    return True


def max_prime_mult(array):
    la = len(array) - 1
    i = 0

    mult = 1
    while i < la:
        if is_prime(array[i]):
            mult *= array[i]
        if array[i + 1] == mult:
            return i + 1

        i += 1

    return None


print(T)
print(max_prime_mult(T))

# 2


def radix_mult_sum(n, r):
    m = 1
    digits = 0
    while m <= n:
        m *= r
        digits += 1
    m = 1
    mult = 1
    i = 0
    while i < digits:
        mult *= n // m % r
        m *= r
        i += 1

    return mult


def rotate(n, digits):
    m = 10 ** (digits - 1)

    take = n // m
    n_new = n - take * m
    return n_new * 10 + take


def digit_count(n):
    m = 10
    digits = 1
    while m <= n:
        m *= 10
        digits += 1
    return digits


def is_prime_mult(n):
    dc = digit_count(n)

    power = 2
    while power <= 16:
        i = 0
        while i < dc:
            if is_prime(radix_mult_sum(n, power)):
                return power
            n = rotate(n, dc)
            i += 1
        power += 1

    return None


print(is_prime_mult(17))
