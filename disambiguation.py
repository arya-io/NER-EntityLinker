import requests

def handle_ambiguous_entity(entity, context=None):
    """
    Handles ambiguous entities by querying Wikipedia and providing options to the user
    to choose the correct entity link. It returns a list of possible links.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={entity}&limit=5&format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if len(data[3]) > 1:
            # If multiple options are found, return them all for the user to choose
            return data[3]  # This returns all the URLs
        elif len(data[3]) == 1:
            return data[3]  # Only one link, no ambiguity
        else:
            return None  # No links found
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
