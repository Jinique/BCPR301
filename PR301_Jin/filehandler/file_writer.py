# Jin
class FileWriter:
    """
    Creates new file from its source(arg1)
    >>> file_write = FileWriter('test1.txt', 'test.txt')
    file_writer initialised...
    >>> print(file_write)
    test1.txt

    """
    def __init__(self, filename, source):
        with open(filename, 'w+') as outf:
            # outf.write(source)
            self.outfname = filename
            print(f"{source}", file=outf)

        print("file_writer initialised...")

    def __str__(self):
        return self.outfname
