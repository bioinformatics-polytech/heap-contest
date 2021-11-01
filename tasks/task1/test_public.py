from typing import List

import pytest

from .task import task1


class Case:
    def __init__(self, name: str, stones: List[int], answer: int):
        self._name = name
        self.stones = stones
        self.answer = answer

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base0',
        stones=[],
        answer=0,
    ),
    Case(
        name='base1',
        stones=[2, 7, 4, 1, 8, 1],
        answer=1,
    ),
    Case(
        name='base2',
        stones=[2, 7, 4, 1, 8],
        answer=0,
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = task1(
        stones=case.stones
    )
    assert answer == case.answer
