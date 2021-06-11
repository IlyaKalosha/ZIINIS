import Hash
import Signatures

if __name__ == '__main__':
    """RSA"""
    data = 'Kalosha'
    priv_key, pub_key = Signatures.generate_keys_RSA()
    sign = Signatures.sign_data_RSA(priv_key, data)
    Signatures.verify_data_RSA(pub_key, sign, 'Kalosha')

    """Schnorr"""
    priv_key, pub_key = Signatures.generate_keys_Schnorr()
    sign = Signatures.sign_data_Schnorr(priv_key, data)
    Signatures.verify_data_Schnorr (pub_key, sign, 'Kalosha')

    """El Gamal"""
    key = Signatures.generate_keys_Elgamal()
    sign = Signatures.sign_data_Elgamal(key, data)
    Signatures.verify_data_Elgamal(key, data, sign)