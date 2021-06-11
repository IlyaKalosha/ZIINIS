import pyDes
import secrets

if __name__ == '__main__':
    key_16 = secrets.token_bytes(16)
    des_EDE = pyDes.triple_des(key_16, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encripted = des_EDE.encrypt(str.encode("Сообщение для шифрования "))
    decripted = des_EDE.decrypt(encripted)
    #print(encripted)
    #print(decripted)
    print(encripted.decode('UTF-16'))
    print(decripted.decode('UTF-8'))
