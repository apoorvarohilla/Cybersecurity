import streamlit as st
from cybersecurity_pipeline import security_pipeline

st.title("Cybersecurity Scanner")
st.write("Enter a target URL/IP and select a security scan to run.")

target = st.text_input("Enter Target URL/IP")
scan_tool = st.selectbox("Select Scan Tool", ["nmap", "gobuster", "sqlmap"])

if st.button("Run Scan"):
    if target:
        logs = security_pipeline([{"tool": scan_tool, "target": target}], ["example.com"])
        st.write("\n".join(logs))
    else:
        st.error("Please enter a target URL/IP before running the scan.")
