import pytest
from Main import GetDiff

# @pytest.fixture()
# def getFiles():


@pytest.mark.parametrize("one, two", [([1, 1], [1, 2])])
def test_diff(one, two):
    assert GetDiff(one, two) == [2]