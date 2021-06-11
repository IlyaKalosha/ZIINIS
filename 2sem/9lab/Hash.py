import Decorators
import hashlib


@Decorators.func_runtime_period
def message_sha3_512_hash(message):
    return hashlib.sha3_512(str.encode(message)).hexdigest()

@Decorators.func_runtime_period
def message_sha2_512_hash(message):
    return hashlib.sha512(str.encode(message)).hexdigest()

@Decorators.func_runtime_period
def message_md5_hash(message):
    return hashlib.md5(str.encode(message)).hexdigest()
