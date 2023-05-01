import socket
import sys

def create_socket(multicast_group: str, multicast_port: int, interface_ip: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
    sock.bind(('', multicast_port))
    sock.setsockopt(
        socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
        socket.inet_aton(multicast_group) +socket.inet_aton(interface_ip))
    return sock

def main():
    multicast_group = sys.argv[1]
    multicast_port = int(sys.argv[2])
    interface_ip = sys.argv[3]
    sock = create_socket(multicast_group, multicast_port, interface_ip)

    print(f'multicast group = {multicast_group}, multicast port = {multicast_port}, interface IP = {interface_ip}')
    print('waiting for messages...')

    while True:
        print(sock.recvfrom(1500))

if __name__ == "__main__":
    main()
