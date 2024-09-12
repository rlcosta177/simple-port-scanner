import socket
from _datetime import datetime

# ip can be string.. python my beloved
target = input("target ip address")


def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f'scanning the target {ip}')
        print('time started', datetime.now())

        # scan the well-known ports only
        for port in range(1, 1023):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # one second time out
            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f'port {port}: open')
            sock.close()

    except socket.gaierror:
        print('hostname could not be resolved')

    except socket.error:
        print('socket error')

    except KeyboardInterrupt:
        sock.close()


port_scan(target)
