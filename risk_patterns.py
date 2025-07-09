risk_terms = {
    "data_sharing": [r"\bshare.*data\b", r"\bthird[- ]party data\b"],
    "no_refund": [r"\bno refunds?\b", r"\bnon[- ]refundable\b"],
    "auto_renewal": [r"\bauto[- ]?renew(al)?\b", r"\bautomatically renewed\b"],
    "waive_rights": [r"\byou waive\b", r"\bright to sue\b"],
    "jurisdiction": [r"\bgoverned by.*(law|jurisdiction)\b"],
    "liability_limit": [r"\blimit our liability\b", r"\bnot responsible\b"],
    "data_storage": [r"\bstored in\b.*(server|cloud|region)"],
}
