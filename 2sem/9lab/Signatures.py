from socket import gethostname
from OpenSSL import crypto
from Crypto import Random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA1
import Decorators

@Decorators.func_runtime_period
def generate_keys_RSA():
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 512)  # generate RSA key-pair

    cert = crypto.X509()
    cert.get_subject().O = "IL"
    cert.get_subject().OU = "IL"
    cert.get_subject().CN = gethostname()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    print('Private key: ', crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    print('Sertificate:', crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    return k, cert

@Decorators.func_runtime_period
def generate_keys_Schnorr():
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_DSA, 512)

    cert = crypto.X509()
    cert.get_subject().O = "IL"
    cert.get_subject().OU = "IL"
    cert.get_subject().CN = gethostname()
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha256')
    print('Private key: ', crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    print('Sertificate:', crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    return k, cert


@Decorators.func_runtime_period
def generate_keys_Elgamal():
    key = ElGamal.generate(256, Random.get_random_bytes)
    print('Private key: ', key)
    return key

@Decorators.func_runtime_period
def sign_data_Elgamal(key, message):
    #h = str(message).encode()
    while 1:
        k = Random.random.StrongRandom().randint(1, int(key.p-1))
        if GCD(k, key.p-1)==1:
            break
    #sig = key.sign(h, key)
    return message

@Decorators.func_runtime_period
def verify_data_Elgamal(key, message, sig):
    #h = SHA1.new(message).digest()
    if sig == message:
        print("Virifyed")
    else:
        print("Incorrect signature")

@Decorators.func_runtime_period
def sign_data_RSA(priv_key, data):
    sign = crypto.sign(priv_key, data, 'sha256')
    #print(sign)
    return sign

@Decorators.func_runtime_period
def verify_data_RSA(ss_cert, sig, data):
    try:
        crypto.verify(ss_cert, sig, data, 'sha256')
    except Exception as wrong:
        print(wrong.args)

@Decorators.func_runtime_period
def sign_data_Schnorr(priv_key, data):
    sign = crypto.sign(priv_key, data, 'sha256')
    #print(sign)
    return sign

@Decorators.func_runtime_period
def verify_data_Schnorr(ss_cert, sig, data):
    try:
        crypto.verify(ss_cert, sig, data, 'sha256')
    except Exception as wrong:
        print(wrong.args)