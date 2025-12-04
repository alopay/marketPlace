from fastapi import FastAPI
from validator import ListRequest, ValidationResponse
from rule_based import rule_based_checks
from llm_validation import llm_checks

app = FastAPI(title="Experian MarketPlace Validator")

@app.post("/validate-listing", response_model=ValidationResponse)
async def validate_list(request: ListRequest):
    rule_score, rule_issues = rule_based_checks(request)
    llm_issues = llm_checks(request)
    all_issues = rule_issues + llm_issues
    compliance_score = max(0, 100 - len(all_issues) * 15)
    
    return ValidationResponse(
        listing_name=request.listing_name,
        compliance_score=compliance_score,
        issues=all_issues
    )