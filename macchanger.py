import subprocess  # Library for executing system commands
import optparse  # Library for parsing command line arguments
import re  # Library for Regular Expression operations


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error(
            "[-] Please specify a New MAC address, use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode()

    # Searching for mac address using Regular Expression
    mac_address_search_result = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address!")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.new_mac)

# Check if the MAC address is actually changed or not
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address changed successfully to " + current_mac)
else:
    print("[-] MAC address did not get changed!")

