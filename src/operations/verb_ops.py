import requests

BASE_URL = "http://localhost:5002/api/verbs"

def get_verbs_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_verbs():
    response = requests.get(BASE_URL)
    return response

def get_verb(verb_id):
    response = requests.get(f"{BASE_URL}/{verb_id}")
    return response

def get_verb_by_name(verb_name):
    response = requests.get(f"{BASE_URL}/{verb_name}")
    return response

def create_verb(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response

def update_verb(verb_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{verb_id}", json=data)
    return response

def delete_verb(verb_id):
    response = requests.delete(f"{BASE_URL}/{verb_id}")
    return response

def get_objects_by_verb(verb_id):
    response = requests.get(f"{BASE_URL}/{verb_id}/objects")
    return response

if __name__ == "__main__":
    pass