from math import isqrt


def prime_factor_count(n):
    pc = 0

    if n == 1:
        return 1

    if n % 2 == 0:
        pc += 1
    while n % 2 == 0:
        n //= 2
        print(n, 2)

    if n % 3 == 0:
        pc += 1
    while n % 3 == 0:
        n //= 3
        print(n, 3)

    div = 5
    while div <= n:
        if n % div == 0:
            pc += 1
        while n % div == 0:
            n //= div
            print(n, div)
        div += 2

    return pc


def prime_factors(n):
    p = [0] * isqrt(n)
    pi = 0

    if n == 1:
        return [1]

    if n % 2 == 0:
        p[pi] = 2
        pi += 1
    while n % 2 == 0:
        n //= 2
        print(n, 2)

    if n % 3 == 0:
        p[pi] = 3
        pi += 1
    while n % 3 == 0:
        n //= 3
        print(n, 3)

    div = 5
    while div <= n:
        if n % div == 0:
            p[pi] = div
            pi += 1
        while n % div == 0:
            n //= div
            print(n, div)
        div += 2

    return p


def mult_prime_factors(pa, pb):
    p = [0] * (len(pa) * len(pb))
    pi = 0
    for pae in pa:
        if pae == 0:
            break
        p[pi] = pae
        pi += 1

    pla = pi

    for pbe in pb:
        if pbe == 0:
            break

        is_new = True
        for pai in range(pla):
            if pa[pai] == pbe:
                is_new = False
                break

        if not is_new:
            continue
        p[pi] = pbe
        pi += 1

    return p


print(prime_factor_count(60))
print(prime_factors(60))
print(mult_prime_factors(prime_factors(15), prime_factors(20)))
