from math import log

# dla kazdej iteracji
# obliczamy styczna: -(f(x) / f'(x)) + x
# dopoki modul f(x) wiekszy od zadanej precyzji


def tangent_est(f, df, s, p):
    x = s
    while abs(f(x)) > p:
        x = -(f(x) / df(x)) + x

    return x


def example_f(x):
    return log(x) + x - 1


def example_df(x):
    return 1 / x + 1


print(tangent_est(example_f, example_df, 0.000_1, 0.000_000_000_1))
print(tangent_est(lambda x: 2**x - 23, lambda x: 2**x * log(2), 0, 0.000_000_000_1))
