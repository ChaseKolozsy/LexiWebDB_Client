import requests

BASE_URL = 'http://localhost:5002/api/enumerated_lemmas'

def get_enumerated_lemmas_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response

def create_enumerated_lemma(*, data: dict):
    response = requests.post(BASE_URL, json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
    return response

def get_all_enumerated_lemmas():
    response = requests.get(BASE_URL)
    return response

def get_enumerated_lemma_by_name(lemma_name):
    response = requests.get(f'{BASE_URL}/{lemma_name}')
    return response

def get_enumerated_lemma_by_base_lemma(base_lemma):
    response = requests.get(f'{BASE_URL}/base_lemma/{base_lemma}')
    return response

def update_enumerated_lemma(enumerated_lemma, data):
    response = requests.put(f'{BASE_URL}/{enumerated_lemma}', json=data, headers={'Content-Type': 'application/json; charset=utf-8'})
    return response

def delete_enumerated_lemma(enumerated_lemma):
    response = requests.delete(f'{BASE_URL}/{enumerated_lemma}')
    return response

def increment_frequency(lemma_name):
    response = requests.post(f'{BASE_URL}/increment_frequency/{lemma_name}')
    return response


if __name__ == '__main__':
    import app_ops
    app_ops.reset_db()
    print(get_enumerated_lemmas_schema())
    print(get_all_enumerated_lemmas())
    dog_1 = {
        'enumerated_lemma': 'dog_1',
        'base_lemma': 'dog',
        'part_of_speech': 'noun',
        'definition': 'a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a retractable claw',
        'frequency': 12345,
        'phrase': 'Look at the dog who is barking',
        'story_link': 'https://www.example.com',
        'media_references': ['filename.mp4'],
        'object_exploration_link': 'https://www.example.com',
        'familiar': True,
        'active': True
    }
    dog_2 = {
        'enumerated_lemma': 'dog_2',
        'base_lemma': 'dog',
        'part_of_speech': 'verb',
        'definition': 'to persistently follow or pursue someone or something, often with negative intentions or in a harassing manner.',
        'frequency': 0,
        'phrase': 'The guy keeps dogging me no matter what I do.',
        'story_link': 'https://www.example.com',
        'media_references': ['filename_1.mp4'],
        'object_exploration_link': 'https://www.example.com',
        'familiar': False,
        'active': False,
        'anki_card_ids': [1, 2, 3]
    }
    dog_3 = {
        'enumerated_lemma': 'dog_3',
        'base_lemma': 'dog',
        'part_of_speech': 'noun',
        'definition': 'a friend or homie',
        'frequency': 77,
        'phrase': "What's up dog?",
        'story_link': 'https://www.example.com',
        'media_references': ['filename_2.mp4'],
        'object_exploration_link': 'https://www.example.com',
        'familiar': True,
        'active': False,
        'anki_card_ids': [88, 99, 111]
    }
    do_1 = {
        'enumerated_lemma': 'do_1',
        'base_lemma': 'do',
        'part_of_speech': 'verb',
        'definition': 'to do',
        'frequency': 0,
    }
    not_1 = {
        'enumerated_lemma': 'not_1',
        'base_lemma': 'not',
        'part_of_speech': 'adverb',
        'definition': 'not',
        'frequency': 0,
    }
    me_1 = {
        'enumerated_lemma': 'me_1',
        'base_lemma': 'me',
        'part_of_speech': 'pronoun',
        'definition': 'you',
        'frequency': 0,
    }
    man_1 = {
        'enumerated_lemma': 'man_1',
        'base_lemma': 'man',
        'part_of_speech': 'noun',
        'definition': 'a human male',
        'frequency': 0,
    }
    enumerated_lemmas = [dog_1, dog_2, dog_3, do_1, not_1, me_1, man_1]
    for enumerated_lemma in enumerated_lemmas:
        print(create_enumerated_lemma(data=enumerated_lemma).json(), '\n')
    #response = get_all_enumerated_lemmas().json()
    #for enumerated_lemma in response['enumerated_lemmas']:
    #    print(enumerated_lemma, '\n')
    print(get_enumerated_lemma_by_base_lemma(base_lemma='dog').json(), '\n\n')
    #print(update_enumerated_lemma(enumerated_lemma='dog_1', data={'frequency': 2}).json(), '\n\n')
    #print(delete_enumerated_lemma(enumerated_lemma='dog_2').json(), '\n\n')
    #print("tryting to get dog_1 by name:", get_enumerated_lemma_by_name(lemma_name='dog_1').json(), '\n\n')
    #print(get_all_enumerated_lemmas().json(), '\n\n')
    #print(increment_frequency(lemma_name='dog_1').json(), '\n\n')
    #print("tryting to get dog_1 by name:", get_enumerated_lemma_by_name(lemma_name='dog_1').json(), '\n\n')
    #lemmas = get_all_enumerated_lemmas().json()
    #for lemma in lemmas['enumerated_lemmas']:
    #    print(lemma, '\n')
    
    
    #print(get_enumerated_lemmas_schema().json(), '\n\n')
    #response = get_all_enumerated_lemmas().json()

    ##for lemma in response['enumerated_lemmas']:
    ##    for key, value in lemma.items():
    ##        print(f'{key}: {value}')
    ##    print('\n\n')


    #response = get_enumerated_lemma_by_base_lemma(base_lemma='egy').json()
    #for lemma in response['enumerated_lemmas']:
    #    for key, value in lemma.items():
    #        if key == 'enumerated_lemma' or key == 'part_of_speech':
    #            print(f'{key}: {value}')
    #    print('\n\n')