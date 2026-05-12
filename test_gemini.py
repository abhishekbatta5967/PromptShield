from llm.prompt_optimizer import analyze_prompt_efficiency

test_prompt = "Explain about AI"

result = analyze_prompt_efficiency(test_prompt)

print("\nFINAL ANALYSIS RESULT:\n")

print(result)
    