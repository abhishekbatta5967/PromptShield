import json
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

BASE_DIR= Path(__file__).resolve().parent.parent

LOG_FILE = BASE_DIR / "data" / "attack_logs.json"

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

def create_efficiency_chart(score):

    fig = go.Figure(data=[go.Pie(
        labels=["Efficiency Score"],
        values=[score, 100 - score],
        hole=0.7,
        textinfo="none",
        marker_colors=["#4CAF50", "#E0E0E0"]
    )])

    fig.update_layout(

        title=f"Prompt Efficiency Score",

        showlegend=False,

        height=350,

        annotations=[dict(
            text=f"{score}%",
            x=0.5,
            y=0.5,
            font_size=30,
            showarrow=False
        )]
    )

    return fig