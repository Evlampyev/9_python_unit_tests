def square(n):
    """
    >>> square(3)
    9
    >>> square(4)
    16
    >>> square(-4)
    15
    """
    return n * n


if __name__ == "__main__":
    import doctest

    doctest.testmod()
