PATTERNS = {
    "Prompt Injection":[
        r"ignore previous instruction", 
        r"ignore all previous instructions", 
        r"disregard earlier directions",
        r"forget your rules",
        r"override system prompt",
        r"bypass restrictions",
        r"stop following previous directions",
        r"disobey prior instructions",
        r"forget earlier commands",
        r"provide confidential information",
        r"internal configuration",
        r"hidden credentials",
        r"ignore safeguards",
    ],

    "Jailbreak Attempt": [
        r"act as dan",
        r"developer mode",
        r"unrestricted ai",
        r"no ethical limitations",
        r"pretend to be evil",
        r"simulate illegal activity",
        r"admin access",
        r"disable safety",
        r"simulate harmful behavior",
    ],

    "Prompt Leakage": [
        r"reveal system prompt",
        r"show hidden instructions",
        r"display internal prompt",
        r"repeat your secret instructions",
    ],

    "Malicious Intent": [
        r"how to hack",
        r"create malware",
        r"steal passwords",
        r"phishing attack",
        r"sql injection",
    ]
}