from clause_parser import extract_clauses
from risk_engine import check_clause_risk

def analyze_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    clauses = extract_clauses(text)
    for i, clause in enumerate(clauses):
        risks = check_clause_risk(clause)
        if risks:
            print(f"[⚠️] Clause {i+1}: {clause}")
            print(f"     → Risk Tags: {', '.join(risks)}\n")
        else:
            print(f"[✅] Clause {i+1}: Safe.\n")

# Run
analyze_text_file("sample_data/dummy_terms.txt")
