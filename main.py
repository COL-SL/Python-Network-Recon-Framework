import argparse
import socket
import threading


def connection_scan(target_ip, target_port):
    """Attempts to create a socket connection with the given IP address and port"""

    """If successful, the port is open. If not, the port is closed"""
    try:
        conn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_socket.connect((target_ip, target_port))
        conn_socket.send(b'Banner_query\r\n')
        print("[+] {}/tcp open".format(target_port))
    except OSError:
        print("[-] {}/tcp closed".format(target_port))
    finally:
        conn_socket.close()  # Ensure the connections is closed


def port_scan(target, port_num):

    t = threading.Thread(target=connection_scan, args=(target, int(port_num)))
    t.start()


def argument_parser():

    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports to "
                                     "scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80, 443'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def study_target(host_target):
    try:
        target_ip = socket.gethostbyname(host_target)
        target_name = socket.gethostbyaddr(target_ip)
    except OSError:
        print("[.] Cannot resolve {}: Unknown host".format(target_ip))
        return  # Exit scan if target IP is not resolved

    print('[*] Study Target IP: {}'.format(target_ip))
    print('[*] Study Target Domain: {}\n'.format(target_name[0]))


if __name__ == '__main__':
    try:

        user_args = argument_parser()
        host = user_args["host"]
        study_target(host)
        port_list = user_args["ports"].split(",")  # Make a list from port numbers
        for port in port_list:
            port_scan(host, port)
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")


