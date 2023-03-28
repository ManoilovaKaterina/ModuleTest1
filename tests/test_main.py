import pytest
from Main import GetDiff, GetSame


@pytest.fixture()
def getReadFiles():
    file1 = 'read_files/file1.txt'
    file2 = 'read_files/file2.txt'
    return file1, file2


@pytest.fixture()
def getWriteFiles():
    file1 = "write_files/diff.txt"
    file2 = "write_files/same.txt"
    return file1, file2


@pytest.mark.parametrize("one, two, exp", [([1, 1], [1, 2], [2]),
                                           ([1, 1], [1, 1],  []),
                                           ([1, 2], [3, 4], [1, 2, 3, 4])])
def test_diff(one, two, exp):
    assert GetDiff(one, two) == exp


@pytest.mark.parametrize("one, two, exp", [([1, 1], [1, 2], [1]),
                                           ([1, 1], [1, 1],  [1]),
                                           ([1, 2], [3, 4], [])])
def test_same(one, two, exp):
    assert GetSame(one, two) == exp