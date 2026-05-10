import json
import os
import pandas as pd
import plotly.express as px

LOG_FILE = "data/attack_logs.json"

def load_logs():

    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()
    
    try:
        with open(LOG_FILE, "r") as f:
            content = f.read().strip()

            if not content:
                return pd.DataFrame()
            
            logs = json.loads(content)

        return pd.DataFrame(logs)

    except Exception:
        return pd.DataFrame()

def severity_chart(df):

    if df.empty:
        return None
    
    fig = px.histogram(df, x="severity", title="Threat Severity Distribution")

    return fig

def threat_type_chart(df):

    if df.empty:
        return None
    
    fig = px.histogram(df, x="threat_type", title="Threat Type Distribution")

    return fig