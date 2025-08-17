import subprocess
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip):
    """
    Mengecek apakah IP aktif dengan ping.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-w", "1000", str(ip)]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def scan_network(network_prefix, max_threads=50):
    """
    Scan jaringan lokal menggunakan ping dengan threading.
    network_prefix: contoh "192.168.1.0/24"
    max_threads: jumlah thread paralel
    """
    net = ipaddress.IPv4Network(network_prefix, strict=False)
    devices = []

    print("Scanning perangkat di jaringan. Mohon tunggu...")

    def check_ip(ip):
        if ping_ip(ip):
            devices.append({"ip": str(ip)})

    with ThreadPoolExecutor(max_threads) as executor:
        for ip in net.hosts():
            executor.submit(check_ip, ip)

    return devices
