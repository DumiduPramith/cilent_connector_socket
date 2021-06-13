import multiprocessing, socket, time
from client import main as c_m

def main():
    check = True
    process = False
    pros_list = []
    while True:
        while check:
            print("start checking")
            try:
                socket.create_connection(('216.58.192.142', 80))
                check = False
            except:
                time.sleep(600)
        if not process:
            p = multiprocessing.Process(target=c_m)
            pros_list.append(p)
            p.start()
            process = True
            print("process started")
        
        if pros_list != []:
            proc = pros_list[0]
            is_alive_ = proc.is_alive()
            if not is_alive_:
                check = True
                process = False
                del pros_list[0]
main()