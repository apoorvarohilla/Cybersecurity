import os
import subprocess
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_nmap_scan(target):
    """Run an nmap scan on the target domain/IP."""
    command = ["nmap", "-sV", target]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        return result.stdout
    except Exception as e:
        logging.error(f"Nmap scan failed: {str(e)}")
        return "Error running nmap"

def run_gobuster_scan(target):
    """Run a gobuster directory scan."""
    command = ["gobuster", "dir", "-u", f"http://{target}", "-w", "/usr/share/wordlists/dirb/common.txt"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
        return result.stdout
    except Exception as e:
        logging.error(f"Gobuster scan failed: {str(e)}")
        return "Error running gobuster"

def enforce_scope(target, allowed_targets):
    """Check if the target is within the allowed scope."""
    return any(target.endswith(domain) for domain in allowed_targets)

def security_pipeline(task_list, scope):
    """Execute security tasks within defined scope."""
    logs = []
    
    for task in task_list:
        target = task["target"]
        tool = task["tool"]
        
        if not enforce_scope(target, scope):
            logs.append(f"Target {target} is out of scope. Skipping...")
            continue
        
        result = ""
        if tool == "nmap":
            result = run_nmap_scan(target)
        elif tool == "gobuster":
            result = run_gobuster_scan(target)
        
        logs.append(f"Executed {tool} on {target}: {result[:200]}...")
    
    return logs

if __name__ == "__main__":
    # Define security tasks
    task_list = [
        {"tool": "nmap", "target": "example.com"},
        {"tool": "gobuster", "target": "example.com"}
    ]
    
    # Define scope to prevent unauthorized scans
    scope = ["example.com"]
    
    # Run the security pipeline
    logs = security_pipeline(task_list, scope)
    
    # Print execution logs
    print("\nExecution Logs:")
    print("\n".join(logs))
