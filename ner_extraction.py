import spacy
import os

# Check if the SpaCy model is installed, and if not, download it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
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
