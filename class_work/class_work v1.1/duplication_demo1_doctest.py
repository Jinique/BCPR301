# Refactoring Workbook Chapter 6 Duplication Challenge 1 (Exercise 14)

# Step 2 - write DocTests outside the existing code

"""
>>> from duplication_demo1 import get_times
>>> get_times(interval=10, duration=10, departure=20)
[10, 10, 20]
>>> get_times(interval=0, duration=10, departure=20) # doctest: +ELLIPSIS
Traceback (most recent call last):
...
duplication_demo1.MissingPropertiesException: monitor interval > 0
"""


def test():
    import doctest
    return doctest.testmod(verbose=True)


if __name__ == "__main__":
    test()
