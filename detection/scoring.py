def get_severity(score):
    if score <= 25:
        return "Low"

    elif score <= 50:
        return "Medium"

    elif score <= 75:
        return "High"

    else:
        return "Critical"