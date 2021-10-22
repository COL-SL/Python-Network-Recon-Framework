import argparse
import socket


def initial_select():
    option_chose = input('Please enter:\n [1] To scan ports with Python\n [2] To scan ports with Nmap\n [3] '
                         'Web Page Scraping\n')
    return option_chose


def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports to "
                                                 "scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80, 443'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args


def study_target(host_target):
    try:
        target_ip_local = socket.gethostbyname(host_target)
        target_name = socket.gethostbyaddr(target_ip_local)
    except OSError:
        print("[.] Cannot resolve {}: Unknown host")
        return  # Exit scan if target IP is not resolved

    print('[*] Study Target IP: {}'.format(target_ip_local))
    print('[*] Study Target Domain: {}\n'.format(target_name[0]))