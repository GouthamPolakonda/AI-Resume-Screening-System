import re
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]',' ',text)
    doc = nlp(text)
    clean_words = []

    for token in doc:
        if not token.is_stop:
            clean_words.append(token.lemma_)

    clean_text = " ".join(clean_words)
    return clean_text