import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

# Initialize the Matcher
matcher = Matcher(nlp.vocab)

# Add a pattern for detecting iPhone models (e.g., iPhone 15)
pattern = [
    {"LOWER": "iphone"},  # Match 'iphone' case insensitive
    {"IS_DIGIT": True}    # Match a number (e.g., 15, 14, etc.)
]
matcher.add("IPHONE_MODEL", [pattern])

def refine_entity_types(text):
    refined_entities = []
    
    # Process the input text with spaCy
    doc = nlp(text)
    
    # Apply rule-based matching to find iPhone models
    matches = matcher(doc)
    
    # For each match, append the product entity type
    for match_id, start, end in matches:
        span = doc[start:end]
        refined_entities.append((span.text, "PRODUCT"))  # iPhone 15 recognized as PRODUCT
    
    # Iterate over each named entity in spaCy's doc
    for ent in doc.ents:
        # Explicitly handle Apple context
        if ent.text.lower() == "apple":
            if "iPhone" in text or "tech" in text or "innovation" in text:
                refined_entities.append((ent.text, "ORG"))  # Apple as tech company
            else:
                refined_entities.append((ent.text, "FOOD"))  # Apple as fruit
        else:
            refined_entities.append((ent.text, ent.label_))  # Keep other entities as is
    
    return refined_entities
