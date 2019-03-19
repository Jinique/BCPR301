class FileReader:
    def __init__(self, filename):
        with open(filename, 'r') as inf:
            self.content = inf.read()
        print(">>> file_reader initialised...")

    def __str__(self):
        return "content of the file are \n\n" + self.content + "\n"
