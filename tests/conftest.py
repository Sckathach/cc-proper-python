import pytest
import source.eudyptes as eudyptes


@pytest.fixture
def bdenneu():
    return eudyptes.Chrysolophus("Bruno")


@pytest.fixture
def bruno():
    return eudyptes.Chrysolophus("Bruno")
