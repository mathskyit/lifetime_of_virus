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
    f = open('signature_db.txt')
    db ={}  
    for line in f:
        key, name = line.split()
        db[key] = name
    f.close()
    return db

def main():
    print get_signature_db()

if __name__ == '__main__':
    main()
##



