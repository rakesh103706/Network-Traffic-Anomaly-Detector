from scapy.all import sniff
import joblib
import pandas as pd

# Load trained model
model = joblib.load("anomaly_model.pkl")

print("🚨 Real-Time Network Anomaly Detector Started...")
print("Monitoring live traffic... (Press Ctrl+C to stop)\n")

def detect_packet(packet):
    if packet.haslayer("IP"):
        packet_size = len(packet)
        src_ip_count = 1  # default value for live packet

        # Prepare data in same format as training
        data = pd.DataFrame([[packet_size, src_ip_count]], 
                            columns=["packet_size", "src_ip_count"])

        prediction = model.predict(data)[0]

        if prediction == -1:
            print(f"⚠️ ALERT: Anomalous packet detected! Size={packet_size}")

# Start sniffing
sniff(prn=detect_packet, store=0)