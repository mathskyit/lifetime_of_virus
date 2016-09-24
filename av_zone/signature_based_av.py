import os
import core_av

# import signature database
sig_db = open('signature_db.txt')
db = {}
for line in sig_db:
    key, name = line.split()
    db[key] = name
print "Dictionary:\n", db
## end import

def scan(path):
    if not os.path.isdir(path):
        print "path not found"
        return
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            scan(file)
        elif file[-3:] == '.py':
            print 'Scanning ', file
            find_virus(file)

def find_virus(file):
    sig = core_av.hash_block(file)
    if sig in db:
        print '\t:( VIRUS FOUND: %s' % (db[sig])
    else:
        print '\tno virus'

def main():
    scan('D:')

if __name__ == "__main__":
    main()
