# ner_extraction.py
import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Function to extract Named Entities
def extract_named_entities(text):
    """
    Extracts named entities from a text using spaCy.
    Returns a list of tuples (entity_text, entity_label).
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Example usage:
# text = "Barack Obama is the president of the United States."
# entities = extract_named_entities(text)
# print(entities)
