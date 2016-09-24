import hashlib
import random
import os


#####
block_size = 200
#####

def hash_block(file, begin=0, size=block_size):
    data = open(file).read()
    text_to_hash = ""
    if len(data) < size:
        text_to_hash = data
    else:
        text_to_hash = data[begin:begin+size]
    return hashlib.md5(text_to_hash).hexdigest()


def get_signature_db():
    sig_db = open('signature_db.txt')
    db = {}
    for line in sig_db:
        key, name = line.split()
        db[key] = name
    return db

def main():
    hash_block(__file__,10)

if __name__ == '__main__':
    main()




