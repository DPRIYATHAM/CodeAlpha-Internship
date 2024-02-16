# Importing the required packages.
import scapy.all
import psutil
from prettytable import PrettyTable
import subprocess
import re
import time
from colorama import Fore
from colorama import Style
from scapy.layers.inet import IP, TCP, UDP, ICMP


# Function to get the current MAC address of the system.
def get_current_mac(interface):
    try:
        output = subprocess.check_output(["ifconfig", interface])
        return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output)).group(0)
    except:
        pass


# Function to get the current IP address of the system.
def get_current_ip(interface):
    output = subprocess.check_output(["ifconfig", interface])
    pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    output1 = output.decode()
    ip = pattern.search(output1)[0]
    return ip


# Function to get IP table of the system.
def ip_table():
    # get all the interface deatils in with psutil in a variable
    addrs = psutil.net_if_addrs()
    t = PrettyTable(
        [f"{Fore.GREEN}Interface", "Mac Address", f"IP Address{Style.RESET_ALL}"]
    )
    for k, v in addrs.items():
        mac = get_current_mac(k)
        ip = get_current_ip(k)
        if ip and mac:
            t.add_row([k, mac, ip])
        elif mac:
            t.add_row([k, mac, f"{Fore.YELLOW}No IP assigned{Style.RESET_ALL}"])
        elif ip:
            t.add_row([k, f"{Fore.YELLOW}No MAC assigned{Style.RESET_ALL}", ip])
    print(t)


# Function to sniff the packets.
def sniff(interface):
    scapy.all.sniff(iface=interface, prn=packet_callback, store=False)


# Packet callback function to process sniffed packets.
def packet_callback(packet):
    # Initialize a formatted string to hold packet details
    packet_details = f"{Fore.CYAN}Packet Details:{Style.RESET_ALL}\n"

    # Check if the packet contains IP layer
    if IP in packet:
        packet_details += f"{Fore.GREEN}IP Layer:{Style.RESET_ALL}\n"
        packet_details += (
            f"Source IP: {packet[IP].src} -> Destination IP: {packet[IP].dst}\n"
        )
        packet_details += f"ID: {packet[IP].id} ; Version: {packet[IP].version} ; Length: {packet[IP].len} ; Flags: {packet[IP].flags}\n"
        packet_details += f"Protocol: {packet[IP].proto} ; TTL: {packet[IP].ttl} ; Checksum: {packet[IP].chksum}\n"

    # Check if the packet contains TCP layer
    if TCP in packet:
        packet_details += f"{Fore.YELLOW}TCP Layer:{Style.RESET_ALL}\n"
        packet_details += f"Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}\n"
        packet_details += f"Sequence Number: {packet[TCP].seq} ; Acknowledgment Number: {packet[TCP].ack}\n"
        packet_details += (
            f"Window: {packet[TCP].window} ; Checksum: {packet[TCP].chksum}\n"
        )
        packet_details += (
            f"Flags: {packet[TCP].flags} ; Options: {packet[TCP].options}\n"
        )

    # Check if the packet contains UDP layer
    if UDP in packet:
        packet_details += f"{Fore.YELLOW}UDP Layer:{Style.RESET_ALL}\n"
        packet_details += f"Source Port: {packet[UDP].sport}\n"
        packet_details += f"Destination Port: {packet[UDP].dport}\n"

    # Check if the packet contains ICMP layer
    if ICMP in packet:
        packet_details += f"{Fore.YELLOW}ICMP Layer:{Style.RESET_ALL}\n"
        packet_details += f"Type: {packet[ICMP].type}\n"
        packet_details += f"Code: {packet[ICMP].code}\n"

    # Print the formatted packet details
    print(packet_details)


# Main function to start the packet sniffer.
def main():
    print(f"{Fore.BLUE}Welcome To Packet Sniffer{Style.RESET_ALL}")
    print(
        f"{Fore.YELLOW}[***] Please Start Arp Spoofer Before Using this Module [***]{Style.RESET_ALL}"
    )
    try:
        ip_table()
        interface = input("[*] Please enter the interface name: ")
        print(get_current_ip(interface))
        print(get_current_mac(interface))
        print("[*] Sniffing Packets...")
        sniff(interface)
        print(f"{Fore.YELLOW}\n[*] Interrupt...{Style.RESET_ALL}")
        time.sleep(3)
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n[!] Stopping the Sniffer...{Style.RESET_ALL}")
        time.sleep(3)


if __name__ == "__main__":
    main()
