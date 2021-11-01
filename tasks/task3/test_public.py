from typing import List

import pytest

from .task import task3


class Case:
    def __init__(self, name: str, k: int, primes: List[int], answer: int):
        self._name = name
        self.k = k
        self.primes = primes
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        k=1,
        primes=[2, 3, 5],
        answer=1,
    ),
    Case(
        name='base2',
        k=12,
        primes=[2, 7, 13, 19],
        answer=32,
    ),
    Case(
        name='base3',
        k=16,
        primes=[2, 3, 5],
        answer=25,
    ),
    Case(
        name='base4',
        k=999999,
        primes=[349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
                409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
                541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
                659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
                733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
                863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
                941, 947, 953, 967, 971, 977, 983, 991, 997],
        answer=94558767749,
    ),

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = task3(
        k=case.k,
        primes=case.primes
    )
    assert answer == case.answer
