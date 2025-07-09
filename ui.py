import streamlit as st
from clause_parser import extract_clauses
from risk_engine import check_clause_risk

st.title("📜 Contract Killer – Risk Analyzer")
uploaded = st.file_uploader("Upload your Terms or Contract (.txt only)")

if uploaded:
    text = uploaded.read().decode("utf-8")
    clauses = extract_clauses(text)

    for i, clause in enumerate(clauses):
        risks = check_clause_risk(clause)
        if risks:
            st.error(f"Clause {i+1}: {clause}")
            st.markdown(f"**⚠️ Risks:** {', '.join(risks)}")
        else:
            st.success(f"Clause {i+1}: Safe")
