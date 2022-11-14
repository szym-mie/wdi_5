# dzialanie sprawdzania
# zamieniamy miejscami a i b
# nastepnie bierzemy reszte dzielenia b przez a do a
# powtarzamy dopoki a = 0 (czyli podzielne), zwracamy b


def nwd(a, b):
    while a != 0:
        t = a
        a = b % a
        b = t
        print(a, b)
    return b


print(nwd(49, 21))
