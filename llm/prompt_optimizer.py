import json 
from google import genai
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

def analyze_prompt_efficiency(user_prompt):

    optimization_prompt = f"""
    You are an advanced Prompt Engineering Expert.

    Analyze the given prompt and evaluate its quality for usage with Large Language Models.

    Evaluate based on:
    - Clarity
    - Specificity
    - Structure
    - Context Quality
    - Goal Definition

    Return ONLY valid JSON.

    JSON Format:
    {{
        "efficiency_score": 0,
        "clarity": 0,
        "specificity": 0,
        "structure": 0,
        "context_quality": 0,
        "goal_definition": 0,
        "suggestions": [],
        "optimized_prompt": ""
    }}

    PROMPT:
    {user_prompt}
    """

    try:

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=optimization_prompt
        )
        
        cleaned_response = response.text.strip()

        cleaned_response = cleaned_response.replace("```json", "")
        cleaned_response = cleaned_response.replace("```", "")

        try:

            parsed_response = json.loads(
                cleaned_response
            )

        except:

            parsed_response = {
                "efficiency_score": 50,
                "clarity": 50,
                "specificity": 50,
                "structure": 50,
                "context_quality": 50,
                "goal_definition": 50,
                "suggestions": [
                    "AI optimization parsing failed."
                ],
                "optimized_prompt": user_prompt
            }

        return parsed_response
    
    except Exception as e:

        return {
            "efficiency_score": None,
            "clarity": None,
            "specificity": None,
            "structure": None,
            "context_quality": None,
            "goal_definition": None,
            "suggestions": [f"Prompt optimization failed: {str(e)}"],
            "optimized_prompt": ("This prompt could not be optimized due to an error. Please review the prompt for potential improvements.")
        }
    
