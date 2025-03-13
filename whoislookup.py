import whois
import re

def whois_lookup():
    input_value = input("Enter an IP address or domain name: ")
    
    # Check if the input is an IP address or a domain name
    if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', input_value):
        # IP address lookup
        try:
            whois_info = whois.whois(input_value)
            print("\nWhois Information:")
            for key, value in whois_info.items():
                if value:
                    print(f"{key}: {value}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Domain name lookup
        try:
            whois_info = whois.whois(input_value)
            print("\nWhois Information:")
            for key, value in whois_info.items():
                if value:
                    print(f"{key}: {value}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    whois_lookup()