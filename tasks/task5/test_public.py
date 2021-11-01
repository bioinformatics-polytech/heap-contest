from typing import List

import pytest

from .task import task5


class Case:
    def __init__(self, name: str, buildings: List[List[int]], answers: List[List[int]]):
        self._name = name
        self.buildings = buildings
        self.answers = answers

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        buildings=[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
        answers=[[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
    ),
    Case(
        name='base2',
        buildings=[[0, 2, 3], [2, 5, 3]],
        answers=[[0, 3], [5, 0]],
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task5(case: Case) -> None:
    answer = task5(
        buildings=case.buildings
    )
    assert answer == case.answers
