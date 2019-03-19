from formatter import Pep8Formatter
import FileWriter

data = Pep8Formatter.pep8_format('../data/test_format.txt')
result = FileWriter('../data/test_format_output.txt', data)
