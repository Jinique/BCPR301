class FileWriter:
    def __init__(self, filename, source):
        with open(filename, 'w+') as outf:
            # outf.write(source)
            self.outfname = filename
            print(f"{source}", file=outf)

        print(">>> file_writer initialised...")

    def __str__(self):
        return self.outfname + " new file has been created... "
