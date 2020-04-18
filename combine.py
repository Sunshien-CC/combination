import math
from typing import *
import utils


def num_combinations(n: int, r: int) -> int:
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def combination_to_index(n: int, r: int, c: List[int]) -> int:
    assert len(c) == r
    assert n >= r

    numbers = list(range(1, n + 1))

    result = 0

    for index in range(r):
        rest = r - 1 - index

        while True:
            number = numbers.pop(0)
            if number < c[index]:
                result += num_combinations(len(numbers), rest)
            elif number == c[index]:
                break

    return result


def index_to_combination(n: int, r: int, i: int) -> List[int]:
    assert n >= r

    result = [0] * r

    numbers = list(range(1, n + 1))

    for index in range(r):
        rest = r - 1 - index

        r0 = 0
        r1 = 0
        while True:
            number = numbers.pop(0)
            r1 += num_combinations(len(numbers), rest)
            # print(r1)
            if r1 > i:
                result[index] = number
                i -= r0
                break
            else:
                r0 = r1

    return result

@utils.timer
def bench_c_6_3():
    n = 6
    r = 3

    for i in range(num_combinations(n, r)):
        print('=' * 10)
        c = index_to_combination(n, r, i)
        print(f'index {i} -> {c}')

        ri = combination_to_index(n, r, c)
        print(f'combination {c} -> {ri}')
        assert ri == i

        print('=' * 10)


if __name__ == "__main__":
    bench_c_6_3()
