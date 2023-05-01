from datetime import datetime, timezone
from time import sleep

import socket
import sys

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_IP, socket.IP_MULTICAST_IF, socket.inet_aton('127.0.0.1'))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    return sock

def send_heartbeat(message: bytes, addr: str, port: int) -> None:
    sock = create_socket()
    sock.sendto(message, (addr, port))

def main():
    while True:
        now = datetime.now(tz=timezone.utc).isoformat()
        print(f'Sending {now}...')
        send_heartbeat(bytes(now, encoding='utf8'), sys.argv[1], int(sys.argv[2]))
        sleep(5)

if __name__ == "__main__":
    main()
