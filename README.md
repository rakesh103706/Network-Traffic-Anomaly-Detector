# 🚨 Network Traffic Anomaly Detector (AI-Based IDS)
## 📌 Overview
This project is an AI-powered Network Traffic Anomaly Detector that captures live network packets, extracts meaningful traffic features, and uses an unsupervised machine learning model (Isolation Forest) to identify abnormal or suspicious traffic patterns in real time. It simulates the core functionality of an Intrusion Detection System (IDS) used in cybersecurity to monitor networks and detect potential threats such as traffic spikes, flooding behavior, and unusual packet activity.

The system works by sniffing packets from the network interface, processing packet-level attributes like packet size and frequency of packets from the same source IP, and then feeding these features into an anomaly detection model. The model classifies traffic as either normal or anomalous, enabling real-time alerting and visualization through a Streamlit dashboard.



## 🎯 Objectives
- Monitor live network traffic  
- Detect abnormal or suspicious packet behavior  
- Simulate an ML-based Intrusion Detection System (IDS)  
- Provide real-time alerts and visualization dashboard  



## 🧠 Core Idea
Capture network packets → Extract traffic features → Train ML model → Detect anomalies → Visualize and alert.



## 🏗️ Project Architecture

Live Network Packets (Scapy)
            ↓
   Feature Engineering
(packet_size, src_ip_count)
            ↓
 Isolation Forest Model
 (Unsupervised ML Detection)
            ↓
 Real-Time Anomaly Prediction
            ↓
 Alerts + Streamlit Dashboard


## ⚙️ Technologies Used
- Python  
- Scapy (Packet Sniffing)  
- Pandas & NumPy (Data Processing)  
- Scikit-learn (Isolation Forest ML Model)  
- Streamlit (Visualization Dashboard)  
- Joblib (Model Serialization)  


## 🤖 Machine Learning Approach
The project uses the Isolation Forest algorithm, an unsupervised anomaly detection technique that isolates outliers in the dataset. Since real-world network data often lacks labeled attack data, this model is suitable for detecting abnormal traffic patterns without prior labeling.

### Model Output
- `1` → Normal Traffic  
- `-1` → Anomalous / Suspicious Traffic 🚨  



## 📊 Features Used for Detection
1. **packet_size** – Large or irregular packet sizes may indicate abnormal activity.  
2. **src_ip_count** – Repeated packets from the same source IP may indicate flooding or scanning behavior.  

These features help identify deviations from normal traffic behavior.



## 🔐 Cybersecurity Relevance
This project demonstrates:
- Intrusion Detection System (IDS) concepts  
- Behavioral anomaly detection using AI  
- Detection of suspicious traffic patterns (e.g., DDoS-like bursts, scanning behavior)  
- Real-time network monitoring  


## 📂 Project Structure
 
network-anomaly-detector/
capture_packets.py   -
Capture live network traffic
preprocess.py           Feature engineering & preprocessing
train_model.py          Train Isolation Forest model
realtime_detector.py    Real-time anomaly detection
app.py                  Streamlit dashboard visualization
network_traffic.csv     Captured raw traffic data
processed_traffic.csv   Preprocessed feature dataset
anomaly_model.pkl       Trained ML model
anomaly_results.csv     Prediction results



## 🚀 Key Features
- Live packet sniffing from network interface  
- Feature extraction for behavioral analysis  
- Unsupervised ML-based anomaly detection  
- Real-time alert generation for suspicious packets  
- Interactive dashboard for visualization and monitoring  


## 📈 Workflow
1. Capture packets using Scapy  
2. Convert raw packets into ML features  
3. Train Isolation Forest model on traffic behavior  
4. Detect anomalous packets in real time  
5. Visualize results using Streamlit dashboard  


## 📄 Use Cases
- Network intrusion detection prototype  
- DDoS traffic pattern simulation  
- Behavioral anomaly detection in enterprise networks  
- Educational cybersecurity and machine learning demonstration project  


## 🧪 Future Improvements
- Detect port scanning patterns  
- Integrate real attack datasets (e.g., CICIDS2017)  
- Add IP reputation / blacklist checking  
- Deploy as a cloud-based IDS monitoring tool  
