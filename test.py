import threading

def ok():
    connected = True
    while connected:
        pass
    print("thread stoped")

x = threading.Thread(target=ok)
x.start()
print(getattr(x))