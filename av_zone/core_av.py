import hashlib
import random
import os

block_size = 300
def hash_block(file):
    data = open(file).read()
    text_to_hash = ""
    if len(data) < block_size:
        text_to_hash = data + (block_size-len(data))*"\n"
    else:
        text_to_hash = data[:block_size]
    return hashlib.md5(text_to_hash).hexdigest()




