import random

def sequence_generator(n):
    arr = []
    arr.append(random.randrange(pow(2,5),pow(2,10)))

    for i in range(1,n,1):
        arr.append(sum(arr)+random.randrange(pow(2,5),pow(2,10)))
    return arr

def public_key_generator(arr, prime):
    module = sum(arr)+50
    newArr = []
    for elem in arr:
        newArr.append(elem * prime % module)
    return newArr

def encode(message, public_key):
    bit_message = []
    encoded_message = []
    for elem in message:
        bit_message.append(bin(ord(elem))[2:].zfill(8))
    print(bit_message)
    for elem in bit_message:
        current_symbol = 0
        for j in range(0,len(elem)):
            if elem[j] == '1':
                current_symbol += public_key[j]
        encoded_message.append(current_symbol)
    return encoded_message


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)


# x = mulinv(b) mod n, (x * b) % n == 1
def mulinv(b, n):
    g, x, _ = egcd(b, n)
    #print(g, x, _)
    if g == 1:
        return x % n

def decode(message, prime, secret_key):
    module = sum(secret_key)+50;
    back_prime = mulinv(prime, module)
    decoded_numbers = []
    decoded_message = []
    for item in message:
        decoded_numbers.append(item * back_prime % module)
    #print(decoded_numbers)
    for item in decoded_numbers:
        current_item = item
        bit_str = ''
        for i in range(len(secret_key)-1, -1, -1):
            if current_item - secret_key[i] >=0:
                bit_str ='1' + bit_str
                current_item = current_item - secret_key[i]
            else:
                bit_str ='0'+bit_str
        decoded_message.append(str(''.join([chr(int(bit_str,2))])))
        result = ''.join(decoded_message)
    return result


if __name__ == '__main__':
    message = 'Kalosha Ilya Valerevich'
    secret_key = sequence_generator(8)
    public_key = public_key_generator(secret_key,31)
    encoded_message = encode(message, public_key)
    decoded_message = decode(encoded_message, 31, secret_key)
    print(secret_key)
    print(public_key)
    print(encoded_message)
    print(decoded_message)


