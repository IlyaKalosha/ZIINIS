from collections import Counter
import numpy as np
from matplotlib import pyplot


class RowCol:

    def row_col_encode(self, path, str_len):
        with open(path, "r", encoding="UTF-8") as file:
            file_string = file.read()

        if len(file_string) % str_len != 0:
            count = str_len - len(file_string) % str_len
            for i in range(0, count):
                file_string += " "

        col_count = int(len(file_string) / str_len)
        print(col_count)
        np_file = np.array(list(file_string)).reshape((str_len, col_count))
        np_file = np.transpose(np_file)
        out_str = ""
        for elem in np_file:
            out_str += ''.join(elem)

        with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\RowCol_encode_output.txt", "a", encoding="UTF-8") as file:
            file.write(out_str)

    def row_col_decode(self, path, str_len):
        with open(path, "r", encoding="UTF-8") as file:
            file_string = file.read()

        col_count = int(len(file_string) / str_len)
        np_file = np.array(list(file_string)).reshape((col_count, str_len))
        np_file = np.transpose(np_file)
        print(np_file)
        out_str = ""
        for elem in np_file:
            out_str += ''.join(elem)

        with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\RowCol_decode_output.txt", "a",
                  encoding="UTF-8") as file:
            file.write(out_str)

    def count_file_symbol(self, path):
        with open(path) as file:
            string = file.read()
        symbols = Counter(list(string))
        pyplot.bar(symbols.keys(), symbols.values())
        pyplot.show()