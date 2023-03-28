import pytest
from Main import GetDiff

# @pytest.fixture()
# def getFiles():


@pytest.mark.parametrize("one, two,  exp", [([1, 1], [1, 2], [2]),
                                            ([1, 1], [1, 1],  []),
                                            ([1, 2], [3, 4], [1, 2, 3, 4])])
def test_diff(one, two, exp):
    assert GetDiff(one, two) == exp