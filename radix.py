# najpierw dowiadujemy ile cyfr ma liczba
# mnozymy dzielnik razy podstawe dopoki wiekszy od liczby
# tworzymy tablice o ilosci cyfr dla konwertowanej liczby
# dla kazdej cyfry w tablicy:
# - dzielimy n przez dzielnik
# - bierzemy reszte z dzielenia przez podstawe
# - mnozymy dzielnik razy podstawe

# inne funkcje (rotujaca) suma cyfr w test.py


def to_radix_array(n, r):
    # zliczenie cyfr
    digits = 0
    mult = 1
    while mult <= n:
        mult *= r
        digits += 1

    # konwersja
    out = [0] * digits
    mult = 1
    for index in range(digits):
        out[index] = n // mult % r
        mult *= r
        index += 1

    return out


# czytaj od tylu [2^0, 2^1, 2^2, ...]
print(101, to_radix_array(101, 2))
print(95, to_radix_array(95, 3))
print(127, to_radix_array(127, 16))
