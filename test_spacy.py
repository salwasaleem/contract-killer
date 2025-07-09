import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This clause waives your rights to a refund.")
for token in doc:
    print(f"{token.text:<12} | POS: {token.pos_:<10} | Dep: {token.dep_}")
