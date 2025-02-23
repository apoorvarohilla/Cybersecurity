# Cybersecurity Pipeline

## Overview
This project is a **Cybersecurity Scanning Pipeline** that automates security scans using **Nmap, Gobuster, and SQLMap**. It includes a **command-line interface (CLI)** and an optional **web dashboard using Streamlit** for ease of use.

---

## **1. Prerequisites**
### Install Required Tools:
Ensure you have the following installed on your system:

- **Python 3.8+** → [Download Python](https://www.python.org/downloads/)
- **Go (for Gobuster)** → [Download Go](https://go.dev/dl/)
- **Nmap** → [Download Nmap](https://nmap.org/download.html)
- **Gobuster** → Install via Go
- **SQLMap** → Install via pip

### **Checking Installations**
```sh
python --version
nmap --version
gobuster --help
sqlmap --version
```

If any command fails, install the required tool.

---

## **2. Installation**

### **Step 1: Clone the Repository**
```sh
git clone https://github.com/yourusername/cybersecurity_pipeline.git
cd cybersecurity_pipeline
```

### **Step 2: Set Up a Virtual Environment**
```sh
python -m venv venv
```

### **Step 3: Activate the Virtual Environment**
#### **Windows (CMD)**
```sh
venv\Scripts\activate
```
#### **Windows (PowerShell)**
```sh
.\venv\Scripts\Activate
```
#### **Linux/Mac**
```sh
source venv/bin/activate
```

### **Step 4: Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **3. Running the Cybersecurity Pipeline**

### **Option 1: Run from CLI**
```sh
python cybersecurity_pipeline.py
```

### **Option 2: Run with Custom Targets**
Modify the `task_list` in `cybersecurity_pipeline.py`:
```python
task_list = [
    {"tool": "nmap", "target": "example.com"},
    {"tool": "gobuster", "target": "example.com"},
    {"tool": "sqlmap", "target": "example.com"}  # New addition
]
```
Run:
```sh
python cybersecurity_pipeline.py
```

---

## **4. Adding a Web Dashboard (Streamlit)**
### **Step 1: Install Streamlit**
```sh
pip install streamlit
```

### **Step 2: Create `dashboard.py`**
```python
import streamlit as st
from cybersecurity_pipeline import security_pipeline

st.title("Cybersecurity Scanner")
target = st.text_input("Enter Target URL/IP")
scan_tool = st.selectbox("Select Scan Tool", ["nmap", "gobuster", "sqlmap"])

if st.button("Run Scan"):
    logs = security_pipeline([{ "tool": scan_tool, "target": target }], ["example.com"])
    st.write("\n".join(logs))
```

### **Step 3: Run the Streamlit Dashboard**
```sh
streamlit run dashboard.py
```

---

## **5. Troubleshooting**

### **Streamlit Not Recognized?**
```sh
pip install --upgrade streamlit
.env\Scripts\streamlit.exe run dashboard.py
```

### **Gobuster Not Recognized?**
```sh
# Install Go first, then:
go install github.com/OJ/gobuster/v3@latest
setx PATH "%PATH%;%USERPROFILE%\go\bin"
```

### **Nmap Not Recognized?**
Ensure Nmap is installed and added to **system PATH**.

---

## **6. Future Enhancements**
✅ More security tools (e.g., Nikto, OpenVAS)  
✅ Export scan reports as JSON/CSV  
✅ Real-time notifications for vulnerabilities

---

## **7. Contributors**
👤 Your Name  
🔗 [GitHub](https://github.com/apoorvarohilla)  
📧 richardapoorva@gmail.com

---

## **8. License**
MIT License. Free to use and modify!

