# ICMP Packet Sender

This is a Python script that sends and receives ICMP (ping) packets using the Scapy library. It allows users to input source and destination IP addresses, then sends an ICMP packet and captures the response. The script logs both sent and received packet details to a file, making it useful for network diagnostics and learning about ICMP communication.

---

## ✨Features

- **Dynamic IP Input**: Allows users to input source and destination IP addresses for ICMP packets.
- **Real-time Packet Sending**: Sends ICMP packets and captures response details (if any).
- **Logging**: Logs both sent and received packet details in a structured format to `packet_logs.txt` for future analysis.
- **Error Handling**: Handles network-related errors and logs them for debugging.

---

## 🛠️ Requirements

- Python 3.x
- Scapy library (for packet manipulation)
- Permissions to run the script (root/administrator, depending on the OS)

---

## Installation

1. **Clone the Repository**:

   Clone the GitHub repository to your local machine:

   git clone https://github.com/Hussein-Ibrahim043/ICMP_Packet_Sender.git

2. **Navigate to the project directory:

   cd ICMP_Packet_Sender

3. **Install the required dependencies:

   pip install -r requirements.txt

---

## 🚀 How to Use
1. **Run the Python Script:
   Launch the script from the terminal:
     python ICMP_packet_sender.py
2. **Provide IP Addresses:
   - You’ll be prompted to enter the Source IP and Destination IP.
- The script will send an ICMP packet from the source to the destination and log the results.
3. **Sample Output:
  After you input the IP addresses, the script will:
    - Send the ICMP packet.
    - Capture and log the response (if received).
    - Store detailed logs of sent and received packets in packet_logs.txt.

---

## 📝 Example Log (packet_logs.txt)

2024-10-06 14:30:12 - Packet sent details: {'Source IP': '192.168.1.10', 'Destination IP': '192.168.1.1', 'TTL': 64, 'ICMP Type': 8, 'ICMP Code': 0}
2024-10-06 14:30:13 - Packet received details: {'Response Source IP': '192.168.1.1', 'Response Destination IP': '192.168.1.10', 'Response TTL': 64, 'ICMP Type': 0, 'ICMP Code': 0}
2024-10-06 14:30:13 - Full packet dump (sent): Ether / IP / ICMP  / Padding
2024-10-06 14:30:13 - Full packet dump (received): Ether / IP / ICMP  / Padding

---

## 🔧 Logging and Debugging
- Logs are saved automatically in `packet_logs.txt` with timestamps.
- These logs include both sent and received packet details as well as any errors encountered during packet transmission.

---

## 🛡️ Security Considerations

- Since ICMP packets are often used for network diagnostics, improper usage can lead to network abuse (e.g., DDoS attacks). Ensure that your use of this script complies with your organization's policies and local laws.
- Administrator/root permissions are required for sending ICMP packets on most systems.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Author

- Hussein Ibrahim (https://github.com/Hussein-Ibrahim043)
