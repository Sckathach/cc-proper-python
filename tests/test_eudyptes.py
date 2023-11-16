import time
import pytest
import source.eudyptes as eudyptes


class TestEudyptes:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.chrysolophus = eudyptes.Chrysolophus("Cody")

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.chrysolophus

    def test_hello(self):
        assert self.chrysolophus.say_hello() == "Hello Cody!"


def test_equal(bdenneu, bruno):
    assert bdenneu == bruno


# Only run slow tests : pytest -m slow
# @pytest.mark.slow
# def test_slow(bdenneu, bruno):
#     time.sleep(5)
#     assert bdenneu == bruno


@pytest.mark.skip(reason="C'est cassé")
def test_casse(bruno):
    assert bruno == 42


@pytest.mark.xfail(reason="Ça va pas marcher")
def test_casse2(bruno):
    assert bruno == 42