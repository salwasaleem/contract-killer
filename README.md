# Contract Killer
Risk analyzer for Terms &amp; Conditions

A simple tool that finds dangerous or unfair clauses in contracts, terms & conditions, or privacy policies.

Just upload a .txt file, and it will highlight any risky parts using NLP and pattern matching.

What it does:

Detects common red flags like:

"We may share your data with third parties"

"You waive your right to sue"

"Fees may change anytime without notice"

Uses regex + NLP + your own rules

Shows flagged sentences in a clean UI

How to use:

Clone this repo:
git clone https://github.com/salwasaleem/contract-killer.git
cd contract-killer

Set up virtual environment:
python -m venv venv
.\venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the tool:
streamlit run ui.py

Upload your .txt contract and see results.

Project Structure:

main.py - Entry point (optional)
ui.py - Streamlit app
clause_parser.py - Breaks contract into clauses
risk_engine.py - Risk checker logic
risk_patterns.py - Risky patterns (regex + NLP)
pdf_reader.py - (Optional) for future PDF reading
sample_data/dummy_terms.txt - Sample T&C file
requirements.txt - Python dependencies

License:

This project uses the MIT License – feel free to use, modify, or build on top of it.

Made by:
Salwa Saleem – https://github.com/salwasaleem
