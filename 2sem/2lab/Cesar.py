import time
from collections import Counter

from matplotlib import pyplot


class Cesar:
    diction = {0: '"', 1: 'A', 2: 'Ą', 3: 'B', 4: 'C', 5: 'Ć', 6: 'D', 7: 'E', 8: 'Ę', 9: 'F', 10: 'G', 11: 'H',
               12: 'I', 13: 'J',
               14: 'K', 15: 'L', 16: 'Ł', 17: 'M', 18: 'N', 19: 'Ń', 20: 'O', 21: 'Ó', 22: 'P', 23: 'Q', 24: 'R',
               25: 'S',
               26: 'Ś', 27: 'T', 28: 'U', 29: 'V', 30: 'W', 31: 'X', 32: 'Y', 33: 'Z', 34: 'Ź', 35: 'Ż', 36: 'a',
               37: 'ą',
               38: 'b', 39: 'c', 40: 'ć', 41: 'd', 42: 'e', 43: 'ę', 44: 'f', 45: 'g', 46: 'h', 47: 'i', 48: 'j',
               49: 'k',
               50: 'l', 51: 'ł', 52: 'm', 53: 'n', 54: 'ń', 55: 'o', 56: 'ó', 57: 'p', 58: 'q', 59: 'r', 60: 's',
               61: 'ś',
               62: 't', 63: 'u', 64: 'v', 65: 'w', 66: 'x', 67: 'y', 68: 'z', 69: 'ź', 70: 'ż', 71: ' ', 72: ',',
               73: '.'
               }

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def cesar_encode(self, path, a, b):
        start_time = time.time()
        with open(path, "r", encoding="UTF-8") as file:
            for line in file:
                result = ''
                for letter in line:
                    for key, value in self.diction.items():
                        if value == letter:
                            new_key = (a * key + b) % len(self.diction)
                            result += self.diction[new_key]
                with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\encode_output.txt", "a",
                          encoding="UTF-8") as outfile:
                    outfile.write(result)
                    outfile.write("\n")
        end_time = time.time()
        print("Encoding time is {0}", end_time - start_time)

    def cesar_decode(self, path, a, b):
        start_time = time.time()
        dict_len = len(self.diction)
        with open(path, "r", encoding="UTF-8") as file:
            for line in file:
                result = ''
                for letter in line:
                    for key, value in self.diction.items():
                        if value == letter:
                            new_key = self.modinv(a, dict_len) * (key + dict_len - b) % dict_len
                            result += self.diction[new_key]
                with open("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\decode_output.txt", "a",
                          encoding="UTF-8") as outfile:
                    outfile.write(result)
                    outfile.write("\n")
        end_time = time.time()
        print("Decoding time is {0}", end_time - start_time)

    def count_file_symbol(self, path):
        string = ''
        with open(path) as file:
            string = file.read()
        symbols = Counter(list(string))
        pyplot.bar(symbols.keys(), symbols.values())
        pyplot.show()
