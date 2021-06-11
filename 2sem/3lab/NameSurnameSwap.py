import numpy as np
from time import time
from collections import Counter
from matplotlib import pyplot


class NameSurnameSwap:

    def swap_encode(self, path, name, surname):
        s_time = time()
        with open(path, "r", encoding="UTF-8") as file:
            file_string = file.read()

        if len(file_string) % (len(name)*len(surname)) != 0:
            count = len(name)*len(surname) - len(file_string) % (len(name)*len(surname))
            for i in range(0, count):
                file_string += " "

        cycle_count =int(len(file_string) / (len(name)*len(surname)))
        start = 0
        end = 0
        out_str = ""
        for i in range(1, cycle_count, 1):
            start = (i-1) * len(name)*len(surname)
            end = i * len(name) * len(surname)
            str_to_encode = file_string[start:end]

            np_str_to_encode = np.array(list(str_to_encode)).reshape(len(name), len(surname))
            np_str_to_encode = np.c_[np_str_to_encode, list(name)]
            sorted_by_name = np_str_to_encode[np_str_to_encode[:, -1].argsort()]
            np_str_to_encode = np.delete(sorted_by_name, -1, axis=1)
            np_str_to_encode = np.r_[np_str_to_encode, [list(surname)]]
            sorted_by_name = np_str_to_encode[:,np_str_to_encode[-1].argsort()]
            np_str_to_encode = np.delete(sorted_by_name, -1, axis=0)
            for elem in np_str_to_encode:
                out_str += ''.join(elem)
        with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\Swap_encode_output.txt", "a",
                      encoding="UTF-8") as file:
            file.write(out_str)
        e_time = time()
        print("Encode time is {0}", e_time - s_time)

    def swap_decode(self, path, name, surname):
        s_time = time()
        with open(path, "r", encoding="UTF-8") as file:
            file_string = file.read()

        cycle_count = int(len(file_string) / (len(name) * len(surname)))
        start = 0
        end = 0
        out_str = ""

        np_name =[item for item in range(0,len(name))]
        for i in list(name):
            np_name.append(i)
        np_name = np.array(np_name).reshape(2,len(name))
        np_name = np_name[:, np_name[-1].argsort()]

        np_surname = [item for item in range(0, len(surname))]
        for i in list(surname):
            np_surname.append(i)
        np_surname = np.array(np_surname).reshape(2, len(surname))
        np_surname = np_surname[:, np_surname[-1].argsort()]

        for i in range(1, cycle_count, 1):
            start = (i - 1) * len(name) * len(surname)
            end = i * len(name) * len(surname)
            str_to_encode = file_string[start:end]

            np_str_to_encode = np.array(list(str_to_encode)).reshape(len(name), len(surname))
            np_str_to_encode = np.r_[np_str_to_encode, [np_surname[0]]]
            sorted_by_surname = np_str_to_encode[:, np_str_to_encode[-1].argsort()]
            np_str_to_encode = np.delete(sorted_by_surname, -1, axis=0)
            np_str_to_encode = np.c_[np_str_to_encode, np_name[0]]
            sorted_by_name = np_str_to_encode[np_str_to_encode[:, -1].argsort()]
            np_str_to_encode = np.delete(sorted_by_name, -1, axis=1)

            for elem in np_str_to_encode:
                 out_str += ''.join(elem)

        with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\Swap_decode_output.txt", "a",
                       encoding="UTF-8") as file:
             file.write(out_str)
        e_time = time()
        print("Decode time is {0}", e_time - s_time)

    def count_file_symbol(self, path):
        with open(path) as file:
            string = file.read()
        symbols = Counter(list(string))
        pyplot.bar(symbols.keys(), symbols.values())
        pyplot.show()