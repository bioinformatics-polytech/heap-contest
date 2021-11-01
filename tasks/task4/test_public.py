from typing import List

import pytest

from .task import task4


class Case:
    def __init__(self, name: str, forecast: List[int], actions: List[int]):
        self._name = name
        self.forecast = forecast
        self.actions = actions

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base0',
        forecast=[],
        actions=[],
    ),
    Case(
        name='base1',
        forecast=[1, 2, 3, 4],
        actions=[-1, -1, -1, -1],
    ),
    Case(
        name='base2',
        forecast=[1, 2, 0, 0, 2, 1],
        actions=[-1, -1, 2, 1, -1, -1],
    ),
    Case(
        name='base3',
        forecast=[1, 2, 0, 1, 2],
        actions=[],
    ),
    Case(
        name='base4',
        forecast=[69, 0, 0, 0, 69],
        actions=[-1, 69, 1, 1, -1]
    ),
    Case(
        name='base5',
        forecast=[10, 20, 20],
        actions=[]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    actions = task4(
        forecast=case.forecast
    )
    assert actions == case.actions
