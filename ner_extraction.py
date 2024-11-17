import spacy

nlp = spacy.load("en_core_web_sm")

def extract_named_entities(text):
    """
    Extracts named entities from a text using spaCy.
    Returns a list of tuples (entity_text, entity_label).
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
