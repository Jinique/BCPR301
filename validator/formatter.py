from autopep8 import fix_file


class Pep8Formatter:
    @staticmethod
    def pep8_format(file):
        try:
            print(fix_file(file))
            return fix_file(file)
        except FileNotFoundError:
            print("Requested file is not available")
        except Exception as e:
            print(e)


class Testing:
    def __init__(self):
        pass

    def test(self):
        print("testing success")
