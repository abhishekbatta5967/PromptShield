import streamlit as st
from detection.classifier import hybrid_threat_analysis

st.set_page_config(
    page_title="PromptShield",
    page_icon="🛡️",
    layout="wide"
)

st.title("PromptShield")
st.subheader("LLM Prompt Threat Detection System")

st.markdown("---")

user_prompt = st.text_area("Enter your prompt here:", height=200, placeholder="Type your prompt here...")

if st.button("Analyze Prompt"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        with st.spinner("Analyzing prompt..."):
            result = hybrid_threat_analysis(user_prompt)

        st.markdown("### Analysis Result")

        if not result["threat_detected"]:
            st.success("✅ Prompt Appears Safe")
        
        else:
            st.error("⚠️ Threat Detected")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Risk Score", result["final_risk_score"], delta=None)

            with col2:
                st.metric("Severity", result["final_severity"], delta=None)
        

            st.markdown("---")

            st.subheader("Detected Threat Types")

            st.warning(result["detected_threats"])
                    
            st.subheader("Detected Threat Categories")

            if result["detected_threats"]:

                for threat in result["detected_threats"]:
                    st.error(threat)

            else:
                st.info("No rule-based threats detected.")

            st.markdown("---")

            st.subheader("Threat Explanation")

            st.write(result["explanation"])

            st.markdown("---")

            st.subheader("Safe Rewrite Suggestion")
            st.info(result["safe_rewrite"])