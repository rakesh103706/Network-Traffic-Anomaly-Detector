import pandas as pd

# Load captured packet data
df = pd.read_csv("network_traffic.csv")

print("📊 Raw Data Preview:")
print(df.head())

# Feature Engineering
# Packet size feature
df["packet_size"] = df["packet_len"]

# Frequency of same source IP (detect flooding behavior)
df["src_ip_count"] = df.groupby("src_ip")["src_ip"].transform("count")

# Drop non-numeric columns (ML needs numbers)
df_model = df[["packet_size", "src_ip_count"]]

# Save processed data
df_model.to_csv("processed_traffic.csv", index=False)

print("\n✅ Preprocessing complete. Saved as processed_traffic.csv")