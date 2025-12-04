# Credit Card Marketplace Validator Assumptions

## Assumptions

1. **Regulatory Standards**
   - Marketplace listings must include:
     - APR disclosure: both introductory and ongoing APR.
     - Fee transparency: annual fee, late fee, foreign transaction fee, etc.
     - Credit requirement: clear eligibility statement.

2. **Input Format**
   - Each listing I assumed should follows a structured JSON schema:
     ```json
     {
       "listing_name": "string",
       "description": "string",
       "features": {
         "APR": "string",
         "Credit Requirement": "string",
         "...": "..."
       }
     }
     ```

3. **LLM Role**
   - The LLM provides semantic validation (e.g., vague descriptions, misleading terms).  
   - It complements — not replaces — the rule-based system.

4. **Output Format**
   - All validations return a **unified response**:
     ```json
     {
       "listing_name": "string",
       "compliance_score": "int",
       "issues": [
         { "problem": "string", "suggestion": "string" }
       ]
     }

5.  **Score Calculation**
   - Compliance score starts at 100.  
   - Each issue deducts 15 points (floor at 0).  
   - Example:
     - 3 issues → 100 - (3 × 15) = 55 compliance score.   ```