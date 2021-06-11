import hashlib
import random
import time
from base64 import b64encode
import matplotlib.pyplot as plt
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


def elgamal_test():
    start = time.time()

    a = random.randint(2, 1024)

    # To fing gcd of two numbers
    def gcd(a, b):
        if a < b:
            return gcd(b, a)
        elif a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    # For key generation i.e. large random number
    def gen_key(q):
        key = random.randint(pow(10, 40), q)
        while gcd(q, key) != 1:
            key = random.randint(pow(10,40), q)
        return key

    def power(a, b, c):
        x = 1
        y = a
        while b > 0:
            if b % 2 == 0:
                x = (x * y) % c;
            y = (y * y) % c
            b = int(b / 2)
        return x % c

    # For asymetric encryption
    def encryption(msg, q, h, g):
        ct = []
        k = gen_key(q)
        s = power(h, k, q)
        p = power(g, k, q)
        for i in range(0, len(msg)):
            ct.append(msg[i])
        print("g^k used= ", p)
        print("g^ak used= ", s)
        for i in range(0, len(ct)):
            ct[i] = s * ord(ct[i])
        return ct, p

    # For decryption
    def decryption(ct, p, key, q):
        pt = []
        h = power(p, key, q)
        for i in range(0, len(ct)):
            pt.append(chr(int(ct[i] / h)))
        return pt

    msg = "Ilya Kalosha"
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    key = gen_key(q)
    h = power(g, key, q)
    print("g used=", g)
    print("g^a used=", h)
    ct, p = encryption(msg, q, h, g)
    print("Original Message=", msg)
    print("Encrypted Maessage=", ct)
    print("Encrypted Maessage p=", p)
    pt = decryption(ct, p, key, q)
    d_msg = ''.join(pt)
    print("Decryted Message=", d_msg)
    end = time.time()
    print("time: {}".format(end-start))

def RSA_test():
    start = time.time()
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().exportKey()
    message = 'Ilya Kalosha'
    message = str.encode(message)

    rsa_public_key = RSA.importKey(public_key)
    rsa_public_key = PKCS1_OAEP.new(rsa_public_key)
    encrypted_text = rsa_public_key.encrypt(message)
    encrypted_text_pr = b64encode(encrypted_text)

    print('encrypted_text: {}'.format(encrypted_text_pr))

    rsa_private_key = RSA.importKey(private_key)
    rsa_private_key = PKCS1_OAEP.new(rsa_private_key)
    decrypted_text = rsa_private_key.decrypt(encrypted_text)

    print('decrypted_text: {}'.format(decrypted_text))
    end = time.time()
    print("time: {}".format(end-start))


def dynamic_a():
    y = []
    t = []
    x = 99999
    n = pow(2,1024)
    a = [item for item in range(5,36,1)]
    start = time.time()
    for item in a:
        y.append(pow(item,x)%n)
        end = time.time()
        t.append(end - start)
    plt.plot(t)
    plt.show()
    print(t)

def dynamic_x():
    y = []
    t = []
    x = [pow(10,3),pow(10,4),pow(10,5),pow(10,6),pow(9,7),pow(10,7)]
    n = pow(2, 10024)
    a = 5
    start = time.time()
    for item in x:
        y.append(pow(a, item) % n)
        end = time.time()
        t.append(end - start)
    plt.plot(x, t)
    plt.show()
    print(t)

def dynamic_n():
    y = []
    t = []
    x = 999999
    n = [pow(2,1024),pow(2,1124),pow(2,1224),pow(2,1324),pow(2,1424),pow(2,1524),pow(2,1624),pow(2,1724),pow(2,1924),pow(2,1924)]
    a = 19
    start = time.time()
    for item in n:
        y.append(pow(a, x) % item)
        end = time.time()
        t.append(end - start)
    plt.plot( t)
    plt.show()
    print(t)


if __name__ == '__main__':
    dynamic_a()
    print()
    print()
    print()
    dynamic_x()
    print()
    print()
    print()
    dynamic_n()
    print()
    print()
    print()
    RSA_test()
    print()
    print()
    print()
    elgamal_test()