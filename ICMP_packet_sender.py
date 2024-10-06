from scapy.all import IP 
from scapy.all import ICMP 
#Responsible for sending packets
from scapy.all import sr1
import logging

# Set up logging to log packet details to a file
logging.basicConfig(filename='packet_logs.txt', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Responsible for sending packets
while True :
    try:
        # Input source and destination IP addresses
        src_ip = input("src >")
        dst_ip = input("dst >")
        
        # Create IP header with source and destination IP
        ip_head = IP(src=src_ip,dst=dst_ip)

        # Set up ICMP options
        icmp_options = ICMP(id=100)
        
        # Create the packet (IP header + ICMP options)
        packet = ip_head / icmp_options

        # Send the packet and capture the response
        packet_sender = sr1(packet)
        
        #print(packet_sender.show())

        # Check if a response is received
        if packet_sender:            
            # Extract details from the packet
            sent_packet_details = {
                "Source IP": src_ip,
                "Destination IP": dst_ip,
                "TTL": packet.ttl,
                "ICMP Type": icmp_options.type,
                "ICMP Code": icmp_options.code,
            }
            received_packet_details = {
                "Response Source IP": packet_sender[IP].src,
                "Response Destination IP": packet_sender[IP].dst,
                "Response TTL": packet_sender.ttl,
                "ICMP Type": packet_sender[ICMP].type,
                "ICMP Code": packet_sender[ICMP].code
            }
            
            # Log the detailed information about the sent and received packets
            logging.info(f"Packet sent details: {sent_packet_details}")
            logging.info(f"Packet received details: {received_packet_details}")
            logging.info(f"Full packet dump (sent): {packet.show(dump=True)}")
            logging.info(f"Full packet dump (received): {packet_sender.show(dump=True)}")
        else:
            # Log when there is no response
            logging.info(f"No response received for packet: {packet.summary()}")
    except Exception as e:
        # Print and log errors
        print("Unresolvable value. Error:", e)
        logging.error(f"Error: {e}")
        continue
