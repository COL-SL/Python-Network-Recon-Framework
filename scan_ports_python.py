import socket
import threading


def connection_scan(target_ip, target_port):
    """Attempts to create a socket connection with the given IP address and port"""

    """If successful, the port is open. If not, the port is closed"""
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((target_ip, target_port))
        conn_socket.send(b'Banner_query\r\n')
        results = conn_socket.recv(100)
        print("[+] {}/tcp open".format(target_port))
        print("[+] {}\n".format(str(results)))  # Print banner grab results
    except OSError:
        print("[-] {}/tcp closed\n".format(target_port))
    finally:
        conn_socket.close()  # Ensure the connections is closed


def port_scan(target, port_num):
    t = threading.Thread(target=connection_scan, args=(target, int(port_num)))
    t.start()