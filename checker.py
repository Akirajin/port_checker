from telnetlib import Telnet


def has_open_port(host, port):
    try:
        with Telnet(host, port, 5) as tn:
            tn.sock_avail()
    except ConnectionRefusedError as e:
        return True
    except Exception as e:
        return False

    return True
