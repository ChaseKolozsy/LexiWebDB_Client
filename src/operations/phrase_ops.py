import requests

BASE_URL = 'http://localhost:5002/phrases'

def create_phrase(data):
    response = requests.post(f'{BASE_URL}', json=data)
    if response.status_code == 200:
        print("Phrase created successfully!")
    else:
        print(f"Error creating phrase: {response.json()}")
    return response

def get_all_phrases():
    response = requests.get(f'{BASE_URL}')
    if response.status_code == 200:
        phrases = response.json()
        print(phrases)
    else:
        print(f"Error getting all phrases: {response.json()}")

def get_phrase_by_name(phrase):
    response = requests.get(f'{BASE_URL}/{phrase}')
    if response.status_code == 200:
        found_phrase = response.json()
        print(found_phrase)
    else:
        print(f"Error getting phrase by name: {response.json()}")

def update_phrase(phrase, data):
    response = requests.put(f'{BASE_URL}/{phrase}', json=data)
    if response.status_code == 200:
        print("Phrase updated successfully!")
    else:
        print(f"Error updating phrase: {response.json()}")

def delete_phrase(phrase):
    response = requests.delete(f'{BASE_URL}/{phrase}')
    if response.status_code == 200:
        print("Phrase deleted successfully!")
    else:
        print(f"Error deleting phrase: {response.json()}")

def increment_phrase_frequency(phrase):
    response = requests.post(f'{BASE_URL}/increment_frequency/{phrase}')
    if response.status_code == 200:
        print("Frequency incremented successfully!")
    else:
        print(f"Error incrementing frequency: {response.json()}")

if __name__ == '__main__':
    import app_ops
    # Example usage of the functions
    phrase = "The dog is awesome"
    create_phrase({
        "phrase": phrase,
        "lemma_references": ["dog_1", "the_1", "awesome_1", "is_1"],
        "media_references": ["media1.mp4", "media2.mp4"],
        "anki_card_ids": [1, 2],
        "familiar": True,
        "frequency": 1
    })

    print("Getting all phrases...\n\n")
    get_all_phrases()

    print("Getting phrase by name...\n\n")
    get_phrase_by_name(phrase)

    print("Updating phrase...\n\n")
    update_phrase(phrase, {"frequency": 2})

    print("Incrementing phrase frequency...\n\n")
    increment_phrase_frequency(phrase)
    
    get_phrase_by_name(phrase)

    response = create_phrase({
        "phrase": phrase,
        "lemma_references": ["dog_1", "the_1", "awesome_1", "is_1"],
        "media_references": ["media1.mp4", "media2.mp4"],
        "anki_card_ids": [1, 2],
        "familiar": True,
        "frequency": 1
    })

    print(f"verifying that phrase was not created twice...{response.json()}\n\n")
    get_phrase_by_name(phrase)

    print("Deleting phrase...")
    delete_phrase(phrase)

    print("\n\nCreating phrase again...")
    create_phrase({
        "phrase": phrase,
        "lemma_references": ["dog_1", "the_1", "awesome_1", "is_1"],
        "media_references": ["media1.mp4", "media2.mp4"],
        "anki_card_ids": [1, 2],
        "familiar": True,
        "frequency": 1
    })

    get_phrase_by_name(phrase)

    app_ops.reset_db()

