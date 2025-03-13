# CUSTOM PACKET SENDER USING SCAPY

import re
from scapy.all import send, IP, TCP, ICMP, UDP   
# srp and sr1 is for layer 2, send for layer 3

def send_packet(src_addr:str , src_port:int , dest_addr:str, 
                dest_port:int, pkt_type:str, pkt_data:str)  -> bool:
    """Create and send a packet based on the provided parameters

    Args:
        src_addr(str) : Source IP address
        src_port(int) : Source Port
        dest_addr(str): Destination IP address
        dest_port(int): Destination Port
        pkt_type(str) : Type of packet (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
        pkt_data(str) : Data in the packet
    Returns:
        bool: True if send successfull, False otherwise
    """    

    if pkt_type == "T":
        pkt = IP(dst=dest_addr,src=src_addr)/TCP(dport=dest_port,sport=src_port)/pkt_data
    elif  pkt_type == "U":
        pkt = IP(dst=dest_addr,src=src_addr)/UDP(dport=dest_port,sport=src_port)/pkt_data
    else:
        pkt = IP(dst=dest_addr,src=src_addr)/ICMP()/pkt_data
    try:
        send(pkt ,verbose = False)   # Hide "Send 1 packets" message on console
        return True
    except:
        return False

import re

def is_valid_url_source():
    """_summary_
    Description: Validate the SOURCE address of the packet.
    Returns:
        src_addr: the valid URL of the entered source address
    """                
    while True:
        global src_addr
        url = input("Enter Source address of Packet: ")  
        regex = re.compile(
            # matches an optional "www." in the domain. OR matches an optional "http://" or "https://" at the beginning of the string.
            r'^(?:https?://)?(?:www\.)?(?:http?://)?'
            # domain...
            r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        match = regex.match(url) 
        if match:
            src_addr = url
            return src_addr
        else:
            print("Invalid URL")
            continue



# function to validate the destination address
def is_valid_url_destination():
    """_summary_
    Description: Validate the DESTINATION address of the packet.
    Returns:
        dest_addr: the valid url of the entered destination address
    """                
    while True:
        global dest_addr
        url = input("Enter Destination address of Packet: ")  
        regex = re.compile(
            # matches an optional "www." in the domain. OR matches an optional "http://" or "https://" at the beginning of the string.
            r'^(?:https?://)?(?:www\.)?(?:http?://)?'
            # domain...
            r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?' 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        match = regex.match(url)
        if match:
            dest_addr = url
            return dest_addr
        else:
            print("Invalid URL")
            continue


# function to validate src_port
def is_valid_port_source():
    """_summary_
    Description: Validate the SOURCE port of the packet. Between 1 and 65535
    Returns:
        src_port: the valid port of the entered source port
    """                
    while True:
        global src_port
        src_port = input("Enter Source Port of Packet: ")
        # check if src_port is a digit and is between 1 and 65535
        if src_port.isdigit() and (1 <= int(src_port) <= 65535):
            src_port = int(src_port)
            return src_port
        else:
            print("Invalid Port")
            continue


    #function to validate dest_port
def is_valid_port_destination():
    """_summary_
    Description: Validate the DESTINATION port of the packet. Between 1 and 65535
    Returns:
        dest_port: the valid port of the entered destination port
    """                
    while True:
        global dest_port
        dest_port = input("Enter Destination Port of Packet: ")
        # check if dest_port is a digit and is between 1 and 65535
        if dest_port.isdigit() and (1 <= int(dest_port) <= 65535):
            dest_port = int(dest_port)
            return dest_port
        else:
            print("Invalid Port")
            continue

    #function to validate the packet type
def is_valid_pkt_type():
    """_summary_
    Description: Validate the packet type. (T)TCP, (U)UDP, (I)ICMP echo request. Note it is case sensitive
    Returns:
        pkt_type: The valid packet type (option selected by user)
    """                
    while True:
        global pkt_type
        pkt_type = input("Enter Type (T) TCP, (U) UDP, (I) ICMP echo request (T/U/I): ").upper()

        # check if pkt_type is "T" or "U" or "I
        if pkt_type == "T" or pkt_type == "U" or pkt_type == "I":
            return pkt_type
        else:
            print("Invalid Packet Type")
            continue

    #function to validate the packet count
def is_valid_pkt_count():
    """_summary_
    Description: Validate the packet count. Between 1 and 65535
    Returns:
        pkt_count: The valid packet count (option selected by user)
    """                
    while True:
        global pkt_count
        pkt_count = input("Enter number of packets to send (1-65535): ")
        # check if pkt_count is a digit and is between 1 and 65535
        if pkt_count.isdigit() and (1 <= int(pkt_count) <= 65535):
            pkt_count = int(pkt_count)
            return pkt_count
        else:
            print("Invalid Packet Count")
            continue

def print_custom_menu():
    """Obtain inputs to create custom packet

    Returns: Nil
    """    
    print("\n************************")
    print("* Custom Packet        *")
    print("************************\n")

    #function to prompt for the source destination address
    is_valid_url_source()

    #function to prompt for the source port
    is_valid_port_source()

    #function to prompt for the destination address
    is_valid_url_destination()

    #function to prompt for the destination port
    is_valid_port_destination()

    #function to prompt for the packet type
    is_valid_pkt_type()
    if pkt_type == "I":
        print("  Note: Port number for ICMP will be ignored")
            
    pkt_data = input("Packet RAW Data (optional, DISM-DISM-DISM-DISM left blank): ")
    if pkt_data == "":
        pkt_data = "DISM-DISM-DISM-DISM"
        
    #function to prompt for the packet count
    is_valid_pkt_count()

    start_now = input("Enter Y to Start, Any other return to main menu: ").upper()

    if start_now == "Y" or start_now == "y": 
        count = 0
        for i in range(pkt_count):
            if send_packet(src_addr, src_port, dest_addr, dest_port, pkt_type, pkt_data):
                count  = count + 1
        print(count , " packet(s) sent" )
    else:
        return

#function to print custom packet menu
print_custom_menu()