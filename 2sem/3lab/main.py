from NameSurnameSwap import NameSurnameSwap
from RowCol import RowCol

if __name__ == '__main__':

    test = RowCol()
    test.row_col_encode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\input.txt", 5)
    test.row_col_decode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\RowCol_encode_output.txt", 5)

    test2 = NameSurnameSwap()
    test2.swap_encode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\input.txt", "ilya", "kalosha")
    test2.swap_decode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\Swap_encode_output.txt", "ilya", "kalosha")
    test2.count_file_symbol("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\input.txt")
    test2.count_file_symbol("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\3lab\\Swap_encode_output.txt")