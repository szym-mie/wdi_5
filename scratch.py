def digit_count(n):
    mult = 1
    count = 0

    while mult <= n:
        mult *= 10
        count += 1

    return count


print(digit_count(1))
