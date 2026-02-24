from scapy.all import sniff
import pandas as pd

packets = []

def process_packet(packet):
    if packet.haslayer("IP"):
        packets.append({
            "src_ip": packet["IP"].src,
            "dst_ip": packet["IP"].dst,
            "packet_len": len(packet)
        })

print("📡 Capturing network packets... (Press Ctrl+C to stop)")

try:
    sniff(prn=process_packet, store=0)
except KeyboardInterrupt:
    print("\n🛑 Stopping capture...")

# Save to CSV
df = pd.DataFrame(packets)
df.to_csv("network_traffic.csv", index=False)

print(f"✅ Captured {len(df)} packets and saved to network_traffic.csv")