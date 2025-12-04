from validator import ListRequest, Issues

def rule_based_checks(request: ListRequest):
    """
    Rule based validation checks
    """
    score = 100
    issues = []
    
    apr = request.features.get("APR", "").lower()
    if "apr" not in apr or "variable" not in apr:
        issues.append(Issues(
            problem="APR disclosure missing or unclear",
            suggestion="State both introductory and ongoing APR clearly"
        ))
        score -= 15

    fees = request.features.get("Annual Fee", "")
    if not fees or "£" not in fees:
        issues.append(Issues(
            problem="Fee transparency missing",
            suggestion="List all applicable fees with amounts"
        ))
        score -= 15

    credit_req = request.features.get("Credit Requirement", "").lower()
    if "good" not in credit_req and "excellent" not in credit_req:
        issues.append(Issues(
            problem="Credit requirement unclear",
            suggestion="Specify eligibility requirements clearly"
        ))
        score -= 15

    return score, issues
