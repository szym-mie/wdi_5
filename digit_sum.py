# okreslamy mnoznik wiekszy od n (mnozymy go razy 10 dopoki nie bedzie wiekszy od n)
# w petli dopoki mnoznik wiekszy od 0:
# - dodajemy n podzielone calkowicie przez mnoznik mod 10 do sumy
# - dzielimy mnoznik razy 10


def digit_sum(n):
    d_sum = 0
    n_rest = n
    mult = 1

    while mult * 10 < n:
        mult *= 10

    while mult >= 1:
        d_sum += n // mult % 10
        mult //= 10

    return d_sum


print(digit_sum(5749))
