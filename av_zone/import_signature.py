import core_av
import os

def import_signature():
    file_name = raw_input("Enter virus file name: ")
    if not os.path.isfile(file_name):
        print "file doesn't exist"
    else:
        signature = core_av.hash_block(file_name)
        db = open('signature_db.txt','a')
        db.write(signature + " " + file_name + "\n")
        db.close()
        print 'import successfull'

import_signature()
