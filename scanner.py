import socket
from datetime import datetime

target = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}")
print("Scan started at:", datetime.now())

open_ports = []

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)
    
    s.close()

print("\nScan complete.")
print(f"Open ports: {open_ports}")
