from typing import List

import pytest

from .task import task2


class Case:
    def __init__(self, name: str, commands: List[str], rec_t: int, answer: int):
        self._name = name
        self.commands = commands
        self.rec_t = rec_t
        self.answer = answer

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base0',
        commands=[],
        rec_t=10,
        answer=0
    ),
    Case(
        name='base1',
        commands=['a', 'a', 'a', 'b', 'b', 'b'],
        rec_t=0,
        answer=6
    ),
    Case(
        name='base2',
        commands=['a', 'a', 'a', 'b', 'b', 'b'],
        rec_t=2,
        answer=8
    ),
    Case(
        name='base3',
        commands=['a', 'a', 'a', 'a', 'a', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
        rec_t=2,
        answer=16
    ),
    Case(
        name='base4',
        commands=['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd'],
        rec_t=2,
        answer=13
    ),
    Case(
        name='base5',
        commands=['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
        rec_t=3,
        answer=10
    )

]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = task2(
        commands=case.commands,
        rec_t=case.rec_t
    )
    assert answer == case.answer
