def merge(a, b):
    ai, bi, i = 0, 0, 0
    o = [0] * (len(a) + len(b))

    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            o[i] = a[ai]
            ai += 1
        else:
            o[i] = b[bi]
            bi += 1
        i += 1

    while ai < len(a):
        o[i] = a[ai]
        ai += 1
        i += 1

    while bi < len(b):
        o[i] = b[bi]
        bi += 1
        i += 1

    return o


def merge_distinct(a, b):
    ai, bi, i = 0, 0, 0
    o = [0] * (len(a) + len(b))

    last_o = -1

    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            if last_o != a[ai]:
                o[i] = a[ai]
                i += 1
            ai += 1
        else:
            if last_o != b[bi]:
                o[i] = b[bi]
                i += 1
            bi += 1

        last_o = o[i - 1]

    while ai < len(a):
        if last_o != a[ai]:
            o[i] = a[ai]
            i += 1
        ai += 1

    while bi < len(b):
        if last_o != b[bi]:
            o[i] = b[bi]
            i += 1
        bi += 1

    return o


print(merge([1, 3, 5, 6], [2, 4, 7, 8, 9]))
print(merge_distinct([1, 3, 5, 6], [1, 2, 4, 6, 8, 9]))

