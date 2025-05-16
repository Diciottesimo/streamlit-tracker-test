import streamlit as st
import gspread
from datetime import datetime

# Authenticate using your service account JSON key
gc = gspread.service_account(filename='optical-scarab-433916-c8-fd00f40a89cb.json')
sheet = gc.open("Sample tracker for Python").sheet1  # or .worksheet("Tab name")

# Streamlit form UI
st.title("📋 Agent Tracker")

name = st.text_input("Enter your name")
status = st.selectbox("Select status", ["Pending", "In Progress", "Completed"])

if st.button("Submit"):
    if name.strip() == "":
        st.warning("Name cannot be empty.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([name, status, timestamp])
        st.success("Data submitted successfully!")
