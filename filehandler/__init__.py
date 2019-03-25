# Jin
from file_reader import FileReader
from file_writer import FileWriter

# from file_writer import FileWriter

file_read = FileReader('./test_input.txt')
print(file_read)

file_write = FileWriter('./test_output.txt', file_read)
# print(file_write)
