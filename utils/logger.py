import json
import os
from datetime import datetime  
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


LOG_FILE = BASE_DIR / "data" / "attack_logs.json"

def save_attack_log(prompt, result):

    log_entry = {
        "timestamp": str(datetime.now()),
        "prompt": prompt,
        "risk_score": result["final_risk_score"],
        "severity": result["final_severity"],
        "threat_type": result["llm_threat_type"],
        "threat_detected":result["threat_detected"]
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    with open(LOG_FILE, "r") as f:
        
        content = f.read().strip()

        if not content:
            logs = []
        else:
            logs = json.loads(content)

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)