import socket
import termcolor

def scan(target, ports):
    print("\n" + "Scanning " +str(target))
    for port in range(1, ports):
        scan_port(target,port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]Port open " +str(port))
        sock.close()
    except:
        pass

targets = input("Enter the targets split with , : ")
ports = int(input("Enter the amount of ports: "))
if ',' in targets:
    print("Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)


