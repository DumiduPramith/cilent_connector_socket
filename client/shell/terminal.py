import struct, json, fcntl, termios, time, select, os, pty, threading, subprocess

tabs = {}
thread_list = []

def set_winsize(fd, row, col, xpix=0, ypix=0):
    winsize = struct.pack("HHHH", row, col, xpix, ypix)
    fcntl.ioctl(fd, termios.TIOCSWINSZ, winsize)

class Read_And_Forward_pty_Output(threading.Thread):
    def __init__(self,sid):
        self.fd = None
        self.sid = sid
        self.Connected = True
        threading.Thread.__init__(self)

    def run(self):
        child_pid, self.fd = pty.fork()
        tabs[self.sid] = self.fd
        # print(
        #     "available terminals", tabs, "threads", threading.active_count()
        # )
        if child_pid == 0:
            # this is the child process fork.
            # anything printed here will show up in the pty, including the output
            # of this subprocess
            subprocess.run('bash')
        else:
            # this is the parent process fork.
            # store child fd and pid
            set_winsize(self.fd, 50, 50)

        from connection_handler import conn
        max_read_bytes = 1024 * 20
        while self.Connected:
            time.sleep(0.01)
            if self.fd:
                timeout_sec = 0.01
                try:
                    (data_ready, _, _) = select.select([self.fd], [], [], timeout_sec)
                except:
                    data_ready = False
                if data_ready:
                    output = os.read(self.fd, max_read_bytes).decode()
                    method = b'__pty_output__|'
                    msg = {
                        "output": output,
                        "sid" : self.sid
                        }
                    output = method + json.dumps(msg).encode('utf-8')
                    conn.send_data(output, 'json')
              
def pty_input_(sid,data):
    """write to the child pty. The pty sees this as if you are typing in a real
    terminal.
    """
    try:
        fd = tabs[sid]
        if fd:
            # print("writing to ptd: %s" % data["input"])
            os.write(fd, data["data"]["input"].encode())
            pass
    except:
        pass

def resize_(sid, data):
    try:
        fd = tabs[sid]
        if fd:
            # print("resize", fd, "sid", sid)
            set_winsize(fd, data["rows"], data["cols"])
    except: pass

def connect_(sid,data):

    t= Read_And_Forward_pty_Output(sid)
    thread_list.append(t)
    t.start()
    
    # print("task started")