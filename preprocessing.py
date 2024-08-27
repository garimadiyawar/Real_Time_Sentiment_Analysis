import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Preprocess text by removing unwanted characters and normalizing
    doc = nlp(text.lower())
    return ' '.join(token.text for token in doc if not token.is_punct and not token.is_stop)
