import streamlit as st
import re
from ner_extraction import extract_named_entities
from entity_linking import get_wikipedia_link
from disambiguation import handle_ambiguous_entity
from entity_refinement import refine_entity_types

def capitalize_proper_nouns(text):
    # Capitalize the first letter of each word
    return ' '.join([word.capitalize() if word.islower() else word for word in text.split()])

# Custom CSS to enhance the look
st.markdown("""
    <style>
    .css-ffhzg2 {  # This controls the text area size and appearance
        font-size: 16px;
        padding: 20px;
        background-color: #f7f7f7;
    }
    .css-1v3fvcr {  # This changes the button style
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
    }
    .css-14xtw13 {  # This controls the title style
        text-align: center;
        font-size: 28px;
        color: #2C3E50;
        margin-bottom: 30px;
    }
    .stTextArea textarea { 
        font-size: 16px;
        padding: 10px;
        border-radius: 8px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Named Entity Recognition & Linking with Disambiguation")
st.markdown("""
    This app uses Natural Language Processing (NLP) to identify and link named entities from your text.
    It provides clickable links to Wikipedia articles for each identified entity and offers disambiguation for ambiguous entities like "Apple".
    """)

st.subheader("Enter Text for NER and Entity Linking:")
input_text = st.text_area("Enter text below:", height=150)

submit_button = st.button(label="Process Text")

reset_button = st.button(label="Clear Text")

if reset_button:
    input_text = ""

with st.spinner("Processing..."):
    if submit_button and input_text:
        try:
            # Step 1: Capitalize proper nouns and extract named entities from the input text
            capitalized_text = capitalize_proper_nouns(input_text)
            entities = extract_named_entities(capitalized_text)

            # Step 2: Refine the entity types
            refined_entities = refine_entity_types(input_text)

            # Step 3: Display the sentence with clickable entities
            st.subheader("Processed Text with Clickable Entities:")

            # Sort the entities by length (longest first) to handle multi-word entities first
            refined_entities_sorted = sorted(refined_entities, key=lambda x: len(x[0]), reverse=True)

            # Initialize the sentence with clickable links
            sentence_with_links = input_text

            # For each refined entity, replace the entity with a clickable link
            for entity, label in refined_entities_sorted:
                # Get the Wikipedia link for each entity
                link = get_wikipedia_link(entity, label)

                # If the link is valid, replace the entity with a hyperlink
                if link:
                    clickable_entity = f'<a href="{link}" target="_blank">{entity}</a>'
                    sentence_with_links = re.sub(rf'(?<!\w){re.escape(entity)}(?!\w)', clickable_entity, sentence_with_links)

            # Display the sentence with clickable links
            st.markdown(sentence_with_links, unsafe_allow_html=True)

            # Step 4: Display the entities and their types
            st.subheader("Extracted Entities and Types:")
            for entity, label in refined_entities:
                st.write(f"Entity: {entity}, Type: {label}")

            # Step 5: Retrieve the corresponding Wikipedia links for the entities
            st.subheader("Entity Links:")
            for entity, label in refined_entities:
                # Handle ambiguous entities
                link = get_wikipedia_link(entity, label)
                if link:
                    st.write(f"Entity: {entity}, Type: {label}, Link: {link}")
                else:
                    # If no direct Wikipedia link is found, handle disambiguation
                    st.write(f"Entity: {entity}, Type: {label}")
                    st.write("No direct link found. Trying disambiguation...")

                    # Check for ambiguous entities
                    ambiguous_link = handle_ambiguous_entity(entity, input_text)
                    if ambiguous_link:
                        st.write(f"Disambiguated Link: {ambiguous_link}")
                    else:
                        st.write("No disambiguated link found.")
        except Exception as e:
            st.error(f"Error occurred while processing the text: {e}")
    elif not input_text:
        st.warning("Please enter some text to process.")
