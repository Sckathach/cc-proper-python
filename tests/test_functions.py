import pytest
import source.functions as f


def test_add():
    r = f.add(2, 3)
    assert r == 5


def test_div():
    r = f.div(4, 2)
    assert r == 2


def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        f.div(10, 0)


@pytest.mark.parametrize('a, b, expected', [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_multiple_add(a, b, expected):
    assert f.add(a, b) == expected
