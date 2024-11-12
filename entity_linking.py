import requests

def get_wikipedia_link(entity, entity_type):
    """
    Queries the Wikipedia API and retrieves the link for the given entity.
    If no link is found, returns None.
    """
    # Special handling for specific products like iPhone
    if entity_type == "PRODUCT" and "iPhone" in entity:
        return "https://en.wikipedia.org/wiki/IPhone"
    
    # Special handling for Apple as an organization (avoid linking to the fruit)
    if entity_type == "ORG" and entity.lower() == "apple":
        return "https://en.wikipedia.org/wiki/Apple_Inc."
    
    # Wikipedia API search query
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={entity}&limit=3&format=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        if len(data[3]) > 0:
            return data[3][0]  # Return the first URL from search results
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None
