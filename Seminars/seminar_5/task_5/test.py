from main import is_prime
import pytest


@pytest.mark.parametrize("test_input,expected", [(7, True),
                                                 (6, True),
                                                 (12, False)])
def test_is_prime(test_input, expected):
    assert (is_prime(test_input) == expected)
