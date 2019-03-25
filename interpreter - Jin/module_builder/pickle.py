import pickle


# Jin
class Pickle:

    """Picking a object and output to a file.
    >>> import pickle
    >>> scores = {'korean': 90, 'english': 95, 'mathematics': 85}

    # >>> with open('test.txt', 'wb') as file:
    # ... pickle.dump(scores, file)
    """

    # >>> pickle.dump(list, f)
    @staticmethod
    def pickling(new_object, outfile):
        with open(outfile, 'wb+') as f:
            for data in new_object:
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def unpickling(source):
        with open(source, "rb") as f:
            data_list = []
            while True:
                try:
                    data = pickle.load(f)
                except EOFError:
                    break
                data_list.append(data)
        print(data_list)
        return


if __name__ == "__main__":
    from doctest import testmod
    testmod()
