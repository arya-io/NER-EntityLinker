# Named Entity Recognition & Wikipedia Entity Linking

This Streamlit app performs Named Entity Recognition (NER) using NLP techniques and links the identified entities to their corresponding Wikipedia pages. It also disambiguates ambiguous entities like "Apple," offering clickable links for better context.

## Features
- Extracts named entities from user input using spaCy.
- Links entities to Wikipedia articles.
- Handles disambiguation for ambiguous entities (e.g., distinguishing between Apple Inc. and apple the fruit).
- User-friendly interface built with Streamlit.
- Supports capitalization for proper noun detection and handling lowercase input.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/arya-io/NER-EntityLinker.git
    ```

2. Navigate to the project directory:
    ```bash
    cd NER-EntityLinker
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.7 or higher
- streamlit
- spacy
- requests
- re (Regular Expression library)
- `./en_core_web_sm-3.8.0.tar.gz` file to be downloaded from github

## Usage

1. Open your terminal and run the Streamlit app.
2. Enter text in the input field provided in the main section.
3. Click on "Process Text" to see extracted entities with clickable links to Wikipedia.
4. For ambiguous entities, the app will attempt to disambiguate and provide the most relevant Wikipedia link.

Example input: 
`Apple Inc. launched the iPhone 15 last week. Microsoft and Apple are leading the tech industry.`

The app will extract entities like **"Apple Inc."**, **"iPhone 15"**, and **"Microsoft"** and link them to relevant Wikipedia pages.

## Screenshots

![App Interface Screenshot](screenshot.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or raise an issue for any improvements or bug fixes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

- [spaCy](https://spacy.io/) for Named Entity Recognition.
- [Streamlit](https://streamlit.io/) for building the app interface.
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) for entity linking.

