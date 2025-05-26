import streamlit as st
import random
import time
from datetime import datetime

# Simulated Blockchain Ledger (in-memory)
blockchain_ledger = []

# Function to simulate sensor data
def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "motion": random.choice(["Yes", "No"]),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# Function to simulate writing to blockchain
def write_to_blockchain(data):
    data_hash = hash(str(data))
    blockchain_ledger.append({**data, "hash": data_hash})
    return data_hash

# Streamlit app UI
st.set_page_config(page_title="IoT + Blockchain Prototype", layout="centered")
st.title("🛰️ Simulated IoT + Blockchain Prototype")

if st.button("Simulate Sensor Reading"):
    data = generate_sensor_data()
    data_hash = write_to_blockchain(data)
    st.success("Sensor data recorded on blockchain!")
    st.json(data)

st.subheader("📦 Blockchain Ledger")
if blockchain_ledger:
    for i, record in enumerate(reversed(blockchain_ledger[-5:]), 1):
        st.markdown(f"**Block #{len(blockchain_ledger) - i + 1}**")
        st.json(record)
else:
    st.info("No data on blockchain yet.")
