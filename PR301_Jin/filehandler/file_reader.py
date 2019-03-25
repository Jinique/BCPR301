# Jin
class FileReader:
    """
    Printing our target file when FileReader Class object is created
    >>> file_read = FileReader('test.txt')
    file_reader initialised...
    >>> print(file_read)
    @startuml
    """
    def __init__(self, filename):
        with open(filename, 'r') as inf:
            self.content = inf.read()
        print("file_reader initialised...")

    def __str__(self):
        return self.content


if __name__ == "__main__":
    from doctest import testmod
    testmod()
