def max_sum(arr):
    s_now = 0
    s = 0

    for elem in arr:
        if s_now + elem >= 0:
            s_now += elem
        else:
            s_now = elem

        if s_now >= s:
            s = s_now

    return s


def max_asc_sum2(arr):
    s_now = 0
    s_start_now = 0
    s_end_now = 0

    s1 = 0
    s1_start = 0
    s1_end = 0

    s2 = 0
    s2_start = 0
    s2_end = 0

    last = 0
    for i in range(len(arr)):
        if s_now + arr[i] >= 0 and arr[i] > last:
            s_now += arr[i]
            s_end_now = i
        else:
            s_now = arr[i]
            s_start_now = i
        last = arr[i]
        if s2 <= s_now < s1:
            s2 = s_now
            s2_start = s_start_now
            s2_end = s_end_now
        if s_now >= s1:
            print(s1, s1_start, s1_end)
            s2 = s1
            s2_start = s1_start
            s2_end = s1_end
            s1 = s_now
            s1_start = s_start_now
            s1_end = s_end_now

    return (s1, s1_start, s1_end), (s2, s2_start, s2_end)


print(max_sum([1, 2, 3, 4, -7, 6]))
print(max_asc_sum2([9, 1, 2, 3, 4, -7, 6]))


# def max_sum(arr):
#     s_now = 0
#     min_now = 0
#     max_now = 0
#
#     s1 = 0
#     s2 = 0
#     min1 = 0
#     max1 = 0
#     min2 = 0
#     max2 = 0
#
#     last = 0
#     for i in range(len(arr)):
#         if s_now + arr[i] >= 0 and arr[i] > last:
#             s_now += arr[i]
#             max_now = i
#         else:
#             s_now = arr[i]
#             min_now = i
#         last = arr[i]
#         if s_now >= s1:
#             s2 = s1
#             min2 = min2
#             max2 = max1
#             s1 = s_now
#             min1 = min_now
#             max1 = max_now
#
#     return (s1, min1, max1), (s2, min2, max2)
#
#
# print(max_sum([6, 5, 1, 2, 3, 4, -7]))
