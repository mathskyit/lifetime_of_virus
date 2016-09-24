import os
import core_av
import time

# import signature database
db = core_av.get_signature_db()
type_scan = 1
## end import

black_list = ['$RECYCLE.BIN', 'System Volume Information','Recovery']
def scan(path):
    if not os.path.isdir(path):
        print "path not found"
        return
    files = os.listdir(path)
    for file in files:
        file_path = path + '/' + file
        if file not in black_list and os.path.isdir(file_path):
            scan(file_path)
        elif file[-3:] == '.py':
            if type_scan == 2:
                print " fdfsdfds"
                slow_scan(file_path)
            else:
                quick_scan(file_path)

def quick_scan(file_path):
    print file_path
    block_size = core_av.block_size
    sig = core_av.hash_block(file_path)
    if sig in db:
        print file_path
        print "\t###########################"
        print "\t:( VIRUS FOUND: %s :( " % (db[sig])
        print "\t###########################"


def slow_scan(file_path):
    print file_path
    block_size = core_av.block_size
    f = open(file_path)
    file_size = len(f.read())
    f.close()
    if file_size <= block_size:
        sig = core_av.hash_block(file_path)
        if sig in db:
            print file_path
            print "\t###########################"
            print "\t:( VIRUS FOUND: %s :( " % (db[sig])
            print "\t###########################"
    else:
        for i in range(0, file_size - block_size):
            sig = core_av.hash_block(file_path,i)
            if sig in db:
                print file_path
                print "\t###########################"
                print "\t:( VIRUS FOUND: %s :( " % (db[sig])
                print "\t###########################"


def main():
    print "######## SCANNING #########"
    path = raw_input("Enter path to scan: ")
    global type_scan
    type_scan = int(raw_input("1. Quick scan\n2. Slow scan\n"))
    begin = time.time()
    scan(path)
    print "######## END SCANNING######"
    print "time: ", time.time() - begin

if __name__ == "__main__":
    main()
