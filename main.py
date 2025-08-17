from scanner import scan_network
from utils import get_hostname
import socket
import ipaddress

def get_local_network():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    network = ipaddress.IPv4Network(local_ip + '/24', strict=False)
    return str(network)

def main():
    network_prefix = get_local_network()
    print(f"Scanning jaringan: {network_prefix} ...\n")

    devices = scan_network(network_prefix)
    
    if devices:
        print(f"Ditemukan {len(devices)} perangkat di jaringan:")
        print("IP\t\tHostname")
        print("-"*30)
        for device in devices:
            hostname = get_hostname(device['ip']) or "-"
            print(f"{device['ip']}\t{hostname}")
    else:
        print("Tidak ada perangkat ditemukan.")

if __name__ == "__main__":
    main()
