import pytest
from problem_3 import main


@pytest.mark.parametrize(
    "lista,expected",
    [
        ([1, 2, 3, 4, 5], 3.0),
        ([6, 7, 8, 9, 11], 8.2),
    ],
)
def test_problem_3(lista, expected):
    assert main(lista) == expected
