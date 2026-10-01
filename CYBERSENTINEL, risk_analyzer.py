def suspicious_location(path):
    if not path:
        return False
    return "\\downloads\\" in path.lower()

def risk_level(score):
    if score == 0:
        return "LOW"
    elif score <=25:
        return "MEDIUM"
    else:
        return "HIGH"


def is_startup_program(path, startup_programs):
    return path.lower() in [
        startup_path.lower()
        for startup_path in startup_programs
    ]

def calculate_risk(path , startup_programs):
    score = 0
    reasons = []
    if suspicious_location(path):
        score += 25
        reasons.append("Executable is located in downloads")

    if is_startup_program(path, startup_programs):
        score += 25
        reasons.append("Executable is registered as a startup program")

    return score, reasons


