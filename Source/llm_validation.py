from validator import ListRequest, Issues
import subprocess
import json

def llm_checks(request: ListRequest):
    prompt = f"""
    Analyze this credit card listing for compliance issues. Return ONLY JSON array.

    CARD: {request.listing_name}
    DESCRIPTION: {request.description}
    FEATURES: {json.dumps(request.features)}

    # CRITICAL CHECKS:
    1. APR disclosure: Must show intro + ongoing rates
    2. Fee transparency: All fees with amounts (£)
    3. Credit requirements: Specific eligibility criteria
    4. Language: No jargon, clear sentences
    5. No prohibited terms: Avoid "guaranteed", "best", "free" without specifics

    # PROHIBITED PHRASES:
    - "Guaranteed approval", "No credit check", "Instant approval"
    - "Best on market", "Unbeatable rates", "Absolutely free" 
    - "Limited-time offer" (without date), "Hidden charges"

    Return format: [{{"problem": "...", "suggestion": "..."}}]
    No other text.
    """
    result = subprocess.run(
        ["ollama", "run", "gemma:2b", prompt],
        capture_output=True,
        text=True,
        timeout=30
    )
    output = result.stdout.strip()
 
    data = json.loads(output)
    issues_data = [data] if isinstance(data, dict) else data
    return [Issues(**issue) for issue in issues_data]