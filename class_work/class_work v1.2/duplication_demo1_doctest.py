# Refactoring Workbook Chapter 6 Duplication Challenge 1 (Exercise 14)

# Step 3 - write get_times DocTests in an individual text file


def test():
    import doctest
    doctest.testfile("duplication_demo1_get_times_doctest.txt", verbose=1)
    doctest.testfile("duplication_demo1_get_times_doctest_again.txt", verbose=1)


if __name__ == "__main__":
    test()
