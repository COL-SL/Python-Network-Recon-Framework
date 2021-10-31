import data_entry
import scan_ports_python
import nmap_scan
import page_scrapin
import phising

if __name__ == '__main__':
    try:
        number_option = int(data_entry.initial_select())
        try:
            user_args = data_entry.argument_parser()

            if number_option == 1:
                host = str(user_args["host"])
                data_entry.study_target(host)
                port_list = user_args["ports"].split(",")  # Make a list from port numbers
                for port in port_list:
                    scan_ports_python.port_scan(host, port)  # To use Python functions
            elif number_option == 2:
                host = str(user_args["host"])
                data_entry.study_target(host)
                port_list = user_args["ports"].split(",")  # Make a list from port numbers
                for port in port_list:
                    print(nmap_scan.nmap_scan(host, port))
            elif number_option == 3:
                page_scrapin.page_scraping()
            elif number_option == 4:
                phising.start_phising()
            else:
                print("Please Enter a correct option")

        except AttributeError:
            print("Error. Please provide the command-line arguments before running.")
    except ValueError:
        print("Please Enter a correct option finis")
