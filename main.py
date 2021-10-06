import nmap
import socket
import threading
import data_entry


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


def study_target(host_target):
    try:
        target_ip = socket.gethostbyname(host_target)
        target_name = socket.gethostbyaddr(target_ip)
    except OSError:
        print("[.] Cannot resolve {}: Unknown host".format(target_ip))
        return  # Exit scan if target IP is not resolved

    print('[*] Study Target IP: {}'.format(target_ip))
    print('[*] Study Target Domain: {}\n'.format(target_name[0]))


def nmap_scan(host_id, port_num):

    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']  # Indicate the type of scan and port number
    result = ("[*] {host} tcp/{port} {state}".format(host=host_id, port=port_num, state=state))

    return result


if __name__ == '__main__':
    data_entry.initial_select()
    try:
        user_args = data_entry.argument_parser()
        host = user_args["host"]
        study_target(host)
        port_list = user_args["ports"].split(",")  # Make a list from port numbers
        for port in port_list:
            # port_scan(host, port) To use Python functions
            print(nmap_scan(host, port))
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")


