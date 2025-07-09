import re
from risk_patterns import risk_terms

def check_clause_risk(clause):
    matched_risks = []
    for category, patterns in risk_terms.items():
        for pat in patterns:
            if re.search(pat, clause, re.IGNORECASE):
                matched_risks.append(category)
    return matched_risks
