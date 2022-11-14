from math import isqrt

# przebieg sprawdzania
# szybkie sprawdzenie mniejsze lub rowne 3
# szybkie sprawdzanie czy modulo 2 lub modulo 3
# pomijanie podzielnosci przez 5 poprzez dodawanie 2 potem 4
# 5, 7, 11, 13, 17, 19, 23, ...


def is_prime(n):
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    div = 5
    while div <= isqrt(n):  # pamietaj o <=
        if n % div == 0:
            return False

        div += 2

        if n % div == 0:
            return False

        div += 4

    return True
