def add(a, b):
    """
    >>> add(2, 3)
    5

    >>> add(100, 200)
    300
    """
    return a + b

#python3 -m doctest -v doctest.py

def add_more(x,y):
    """ add together x and y
    >>> add(1,2)
    3

    >>> add(8,"hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return x + y


def double(values):
    """double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double([a,b,c])
    [aa, bb, cc]

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * element for element in values]