import requests

BASE_URL = 'http://localhost:5002/api/phrases'

def create_phrase(data):
    response = requests.post(f'{BASE_URL}', json=data)
    return response

def get_all_phrases():
    response = requests.get(f'{BASE_URL}')
    return response

def get_phrase_by_name(phrase):
    response = requests.get(f'{BASE_URL}/{phrase}')
    return response

def update_phrase(phrase, data):
    response = requests.put(f'{BASE_URL}/{phrase}', json=data)
    return response

def delete_phrase(phrase):
    response = requests.delete(f'{BASE_URL}/{phrase}')
    return response

def increment_phrase_frequency(phrase):
    response = requests.post(f'{BASE_URL}/increment_frequency/{phrase}')
    return response

if __name__ == '__main__':
    pass