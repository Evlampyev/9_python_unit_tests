from unittest import TestCase, main
import pytest
from main import Next


def test():
    with pytest.raises(ZeroDivisionError):
        Next.divide(4, 0)


# def test_1():
#     assertEquals(Next.divide(4, 2), 2)

@pytest.mark.parametrize("a, b, expected", [(10, 0, 0),
                                            (2, 3, 6)])  # Умножение 2 на 3
def test_multiply(a, b, expected):
    assert (Next.multiply(a, b) == expected)

#
# if __name__ == "__main__":
#     main()
