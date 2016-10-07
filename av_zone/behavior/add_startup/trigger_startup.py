import win32event, win32api, win32con
 
print "Monitoring..."

hive = win32con.HKEY_CURRENT_USER
key = 'Software\Microsoft\Windows\CurrentVersion\Run'
handle = win32api.RegOpenKeyEx(hive, key, 0, win32con.KEY_NOTIFY)

win32api.RegNotifyChangeKeyValue(handle,
                                 True,
                                 win32api.REG_NOTIFY_CHANGE_LAST_SET,
                                 None,
                                 False)

print "Have a program add to start-up!"


