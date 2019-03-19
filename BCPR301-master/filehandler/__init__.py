from file_reader import FileReader
from file_writer import FileWriter

# grab file in the args
file_read = FileReader('../data/test_input.txt')
print(file_read)

# args1 = new file name // args2 = input source
file_write = FileWriter('../data/test_output.txt', file_read)
print(file_write)
