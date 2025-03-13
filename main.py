#   MAIN MENU


#   AHMED SHAHEED
#   2109828


# References:
#     https://pythonspot.com/ftp-client-in-python/
#     https://www.geeksforgeeks.org/ftp-in-python/
#     https://www.geeksforgeeks.org/nmap-python-port-scanner/
#     https://www.geeksforgeeks.org/python-program-to-create-a-custom-packet/
#     https://www.geeksforgeeks.org/design-a-keylogger-in-python/

    

# Additional modules to install:
    # nmap
    # scapy
    # tabulate
    # re
    # keyboard




import os

print("**PSEC Info Security Apps**")
menu_options = {
    1: ("Scan network"), 
    2: ("Upload/download file using FTP"), 
    3: ("Send custom packet"),
    4: ("Whois Lookup"),
    5: ("Keylogger"),
    7: ("Check Password Strength"),
    8: ("Quit")
}


while True:
    # DISPLAYING MAIN MENU
    for key in menu_options:
        print(f'{key})',menu_options[key])

    menu_choice = input("\nEnter your choice: ")
    
    if menu_choice == "1": 
        os.system('python nmap_scan.py')


    elif menu_choice == "2":
        os.system('python ftp_client.py')


    elif menu_choice == "3":
        os.system('python custom_packet.py')


    elif menu_choice == "4":
        os.system('python whoislookup.py')


    elif menu_choice == "5":
        os.system('python keylogger.py')


    elif menu_choice == "6":
        os.system('python contact.py')


    elif menu_choice == "7":
        os.system('python password_checker.py')

    elif menu_choice == "8":
        break


    elif menu_choice in menu_options:
        print("You selected", menu_options[menu_choice])
    else:
        print("Invalid choice. Please try again.\n")