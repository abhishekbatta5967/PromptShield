from detection.rule_engine import rule_based_detection
from detection.scoring import get_severity
from llm.gemini_analyzer import analyze_prompt

def hybrid_threat_analysis(user_prompt):

    rule_result = rule_based_detection(user_prompt)
    llm_result = analyze_prompt(user_prompt)

    llm_score = llm_result.get("risk_score", 0)

    try:
        llm_score = int(llm_score)
    except:
        llm_score = 0

    combined_score = (
        rule_result["risk_score"] + llm_score
    ) // 2

    final_severity = get_severity(combined_score)

    return {
        "detected_threats": rule_result["detected_threats"],
        "llm_threat_type": llm_result.get("threat_type"),

        "final_risk_score": combined_score,

        "final_severity": final_severity,

        "explanation": llm_result.get("explanation"),

        "safe_rewrite": llm_result.get("safe_rewrite"),

        "threat_detected": llm_result.get("threat_detected")
    }