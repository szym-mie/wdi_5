from math import isqrt

# sposob dzialania sita
# utworz tablice ktore sa pierwszymi
# zmienna przechowujaca ile pozostalo pierwszymi
# dla kazdej liczby wiekszej od 1 i mniejszej od pierwiastka z n:
# - jezeli dana liczba jest pierwsza (True w tablicy):
# -- dla kazdej wielokrotnosci liczby pierwszej:
# --- jezeli jeszcze zaznaczone ze pierwsza w tablicy:
# ---- ustawiamy na False
# ---- zmniejszamy ilosc pierwszych o 1
# -- zwiekszamy indeks o liczbe pierwsza
# potem tworzymym tablice o ilosci liczb pierwszych - 2 (wylaczamy 0 i 1)
# dla kazdej liczby w zakresie od 2 do n:
# - sprawdzamy czy pierwsza w tablicy
# - dodajemy do tablicy wyjsciowej


def sieve(n):
    p = [True] * n
    pc = n

    for m in range(2, isqrt(n) + 1):  # pamietaj o isqrt(n) + 1
        if p[m]:
            j = m + m
            while j < n:
                if p[j]:
                    p[j] = False
                    pc -= 1
                j += m

    o = [0] * (pc - 2)
    oi = 0
    for m in range(2, n):
        if p[m]:
            o[oi] = m
            oi += 1

    return o


print(sieve(26))
