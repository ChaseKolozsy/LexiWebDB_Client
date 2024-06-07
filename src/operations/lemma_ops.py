import requests

BASE_URL = 'http://127.0.0.1:5000/lemmas'

def get_lemmas_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response.json()

def create_lemma(*, lemma: str, frequency: int, enumerated_lemmas: list[str]):
    """
    Creates a new lemma in the database.
    enumerated lemmas should take the form of lemma_n where n is an int
    """
    data = {
        'lemma': lemma,
        'frequency': frequency,
        'enumerated_lemmas': enumerated_lemmas
    }
    response = requests.post(f'{BASE_URL}/lemmas', json=data)
    return response.json()

def get_all_lemmas():
    response = requests.get(BASE_URL)
    return response.json()

def update_lemma(*, lemma: str, data: dict):
    response = requests.put(f'{BASE_URL}/{lemma}', json=data)
    return response.json()

def delete_lemma(*, lemma: str):
    response = requests.delete(f'{BASE_URL}/{lemma}')
    return response.json()

if __name__ == '__main__':
    print(get_lemmas_schema())
    print(create_lemma(lemma='test', frequency=1, enumerated_lemmas=['test_1']))
    print(get_all_lemmas())
    print(update_lemma(lemma='test', data={'frequency': 2}))
    print(delete_lemma(lemma='test'))

