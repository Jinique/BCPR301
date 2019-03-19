from autopep8 import fix_file


class Pep8Formatter:
    def __init__(self):
        pass

    @staticmethod
    def pep8_format(file):
        try:
            print(fix_file(file))
            return fix_file(file)
        except FileNotFoundError:
            print("Requested file is not available")
        except Exception as e:
            print(e)
