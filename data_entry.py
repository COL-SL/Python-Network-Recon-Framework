import argparse


def initial_select():
    print('Please enter:\n [1] To scan ports with Python\n [2] To scan ports with Nmap\n [3] Web Page Scraping\n')


def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and list of ports to "
                                                 "scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated port list, such as '25,80, 443'")

    var_args = vars(parser.parse_args())  # Convert argument namespace to dictionary

    return var_args
