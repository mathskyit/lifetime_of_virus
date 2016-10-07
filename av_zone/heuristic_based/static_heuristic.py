import os
import time

###
db = {}

def get_db():
    global db
    f = open('evaluation_db.txt')
    for line in f:
        command, level = line.split()
        db[command] = int(level)
    f.close()

def scan(path):
    if not os.path.isdir(path):
        print "path not found"
        return
    files = os.listdir(path)
    for file in files:
        file_path = path + '/' + file
        if os.path.isdir(file_path):
            scan(file_path)
        elif file[-3:] == '.py':
            warm_level = evaluate(file_path)
            print "\tWarm level: %s" % (warm_level)
            if warm_level > 3:
                print "\t######################"
                print "\t:( VIRUS FOUND: %s :( "
                print "\t######################"

def split(string):
    words = []
    i = 0
    while i < len(string):
        while i < len(string) and not string[i].isalpha():
            i += 1
        j = i + 1
        while j < len(string) and (string[j].isalpha() or string[j]=='.'):
            j += 1
        words.append(string[i:j])
        i = j + 1
    return words

def evaluate(file):
    print file
    f = open(file)
    warm = 0
    for line in f:
        words = split(line)
        for word in words:
            if word in db:
                warm += db[word]
    return warm

def main():
    print "######## SCANNING #########"
    path = raw_input("Enter path to scan: ")
    begin = time.time()
    get_db()
    scan(path)
    print "######## END SCANNING######"
    print "time: ", time.time() - begin

if __name__ == '__main__':
    main()
    #print split("fddfd/fdf///fdfdf(fdf)   ")
