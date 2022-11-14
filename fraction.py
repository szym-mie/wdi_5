m = 1700
n = 7

frac_len = 100
i = 0
while i < frac_len:
    print(m // n % 10)
    m *= 10
    i += 1
