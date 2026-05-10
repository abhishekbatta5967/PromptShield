import re
from detection.regex_patterns import PATTERNS

def rule_based_detection(prompt):

    detected_threats = []
    risk_score = 0

    prompt_lower = prompt.lower()

    for category, patterns in PATTERNS.items():

        for pattern in patterns:
            if re.search(pattern, prompt_lower):
                detected_threats.append(category)

                if category == "Prompt Injection":
                    risk_score += 25

                elif category == "Jailbreak Attempt":
                    risk_score += 30

                elif category == "Prompt Leakage":
                    risk_score += 35

                elif category == "Malicious Intent":
                    risk_score += 40

    detected_threats = list(set(detected_threats))

    return {
         "detected_threats": detected_threats,
        "risk_score": min(risk_score, 100)
    }
