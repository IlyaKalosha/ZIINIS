from Cesar import Cesar
from Porta import Porta


if __name__ == '__main__':
    test = Cesar()
    test.cesar_encode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\input.txt", 5, 7)
    test.cesar_decode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\encode_output.txt", 5, 7)
    test.count_file_symbol("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\input.txt")
    test.count_file_symbol("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\encode_output.txt")


    test2 = Porta()
    test2.porta_encode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\input.txt")
    test2.porta_decode("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\porta_encode_output.txt")
    test2.count_file_symbol("C:\\Users\\kalos\\Documents\\3kurs\\OZI\\lab\\2lab\\input.txt")
