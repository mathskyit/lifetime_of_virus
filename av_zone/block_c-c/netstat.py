import os
import time

black_list = '127.0.0.1:50007'
def netstat():
    output = os.popen('netstat -aon').read()
    return output

def main():
    print "Monitoring ................."
    while 1:
        output = netstat()
        if output.find(black_list) != -1:
            print "Warning!!! Virus"
        time.sleep(1)

if __name__ == '__main__':
    main()


    

