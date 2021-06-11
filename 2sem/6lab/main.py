from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes

def seedLCG(initVal):
    global rand
    rand = initVal

def lcg(a, c, m):
    global rand
    rand = (a*rand + c) % m
    return rand

seedLCG(2)

def arc4enc(msg, key):
    tempkey = SHA.new(key).digest()
    cipher = ARC4.new(tempkey)
    msg = cipher.encrypt(msg)
    return  msg

def arc4dec(msg, key):
    tempkey = SHA.new(key).digest()
    cipher = ARC4.new(tempkey)
    msg = cipher.decrypt(msg)
    return msg

if __name__ == '__main__':
    for i in range(10):
        print(lcg(421, 1663, 7875))

    msg = str.encode('Hello World', 'utf-8')
    key = str.encode('1231254184203', 'utf-8')
    res = arc4enc(msg, key)
    print(res)
    res = arc4dec(res, key)
    print(str(res,"UTF-8"))