import math
from math import gcd as nod


def count2_nod(x, y):
    return nod(x, y)


def count3_nod(x, y, z):
    x_y_nod = count2_nod(x, y)
    return nod(x_y_nod, z)


def eratosfen(n):
    list = []
    k=0

    for i in range(2,n+1):
        for j in range (2,i):
            if i%j==0:
                k=k+1
        if k == 0:
            list.append(i)
        else:
            k = 0
    legend =n/math.log(n)
    print("Prime numbers count: ", len(list))
    print("n/ln(n): ", legend)
    print("Accuracy: ",legend/len(list))
    return list


def eratosfenNM(n, m):
    list = []
    k=0

    for i in range(n,m+1):
        for j in range (2,i):
            if i%j==0:
                k=k+1
        if k == 0:
            list.append(i)
        else:
            k = 0
    legend =(m-n)/math.log(m-n)
    print("Prime numbers count: ", len(list))
    print("n/ln(n): ", legend)
    print("Accuracy: ",legend/len(list))
    return list


def canon(number):
    lst = []
    while number>=2:
        for i in range(2,number+1):
            if number%i == 0:
                lst.append(i)
                number = int(number / i)
                break
        number = number
    return lst


if __name__ == '__main__':
    while True:
        x = 0
        print("Enter operation")
        print("1 - 2 num NOD")
        print("2 - 3 num NOD")
        print("3 - prime numbers")
        print("4 - prime numbers(n,m)")
        print("5 - canon")
        print("0 - EXIT")
        x = int(input())

        if x == 1:
            print("Enter first number")
            a = int(input())
            print("Enter second number")
            b = int(input())

            print(count2_nod(a, b))
        elif x == 2:
            print("Enter first number")
            aa = int(input())
            print("Enter second number")
            bb = int(input())
            print("Enter third number")
            cc = int(input())

            print(count3_nod(aa, bb, cc))
        elif x == 3:
            print("Enter high border")
            y = int(input())

            print(eratosfen(y))
        elif x == 4:
            print("Enter low border")
            n = int(input())
            print("Enter high border")
            m = int(input())

            print(eratosfenNM(n, m))
        elif x == 5:
            print("Enter number")
            number = int(input())
            print(canon(number))
        elif x == 0:
            break
