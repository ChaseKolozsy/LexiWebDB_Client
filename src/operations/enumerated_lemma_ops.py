import requests

BASE_URL = 'http://localhost:5002/enumerated_lemmas'

def get_enumerated_lemmas_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response.json()

def create_enumerated_lemma(*, data: dict):
    response = requests.post(BASE_URL, json=data)
    return response.json()

def get_all_enumerated_lemmas():
    response = requests.get(BASE_URL)
    return response.json()

def update_enumerated_lemma(enumerated_lemma, data):
    response = requests.put(f'{BASE_URL}/{enumerated_lemma}', json=data)
    return response.json()

def delete_enumerated_lemma(enumerated_lemma):
    response = requests.delete(f'{BASE_URL}/{enumerated_lemma}')
    return response.json()

if __name__ == '__main__':
    print(get_enumerated_lemmas_schema())
    print(get_all_enumerated_lemmas())
    #dog_1 = {
    #    'enumerated_lemma': 'dog_1',
    #    'part_of_speech': 'noun',
    #    'definition': 'a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a retractable claw',
    #    'frequency': 12345,
    #    'phrase': 'Look at the dog who is barking',
    #    'story_link': 'https://www.example.com',
    #    'media_excerpts': 'filename.mp4',
    #    'object_exploration_link': 'https://www.example.com',
    #    'familiar': True 
    #}
    #dog_2 = {
    #    'enumerated_lemma': 'dog_2',
    #    'part_of_speech': 'verb',
    #    'definition': 'to persistently follow or pursue someone or something, often with negative intentions or in a harassing manner.',
    #    'frequency': 0,
    #    'phrase': 'The guy keeps dogging me no matter what I do.',
    #    'story_link': 'https://www.example.com',
    #    'media_excerpts': 'filename_1.mp4',
    #    'object_exploration_link': 'https://www.example.com',
    #    'familiar': False 
    #}
    #dog_3 = {
    #    'enumerated_lemma': 'dog_3',
    #    'part_of_speech': 'noun',
    #    'definition': 'a friend or homie',
    #    'frequency': 77,
    #    'phrase': "What's up dog?",
    #    'story_link': 'https://www.example.com',
    #    'media_excerpts': 'filename_2.mp4',
    #    'object_exploration_link': 'https://www.example.com',
    #    'familiar': True 
    #}
    #enumerated_lemmas = [dog_1, dog_2, dog_3]
    #for enumerated_lemma in enumerated_lemmas:
    #    print(create_enumerated_lemma(data=enumerated_lemma))
    #print(get_all_enumerated_lemmas())
    #print(update_enumerated_lemma(enumerated_lemma='dog_1', data={'frequency': 2}))
    #print(delete_enumerated_lemma(enumerated_lemma='dog_2'))
    #print(get_all_enumerated_lemmas())

