
def main():
    from connection_handler import conn
    from make_authentication import authenticate
    import time
    CONNECTED = True
    is_authenticated = False
    has_id = False
    sended_time = time.time()

    while CONNECTED:
        C = conn.run()
        if C is False:
            CONNECTED = C
        if not is_authenticated:
            if not has_id:
                if time.time() > sended_time:   
                    send_id = authenticate() #return false if authenticated
                    if send_id is True:
                        sended_time = time.time() + 3
                    elif send_id is False:
                        is_authenticated = True           

if __name__ == "__main__":
    main()