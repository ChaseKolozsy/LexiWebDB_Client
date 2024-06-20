import requests

BASE_URL = "http://localhost:5002/api/states"

def get_states_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_states():
    response = requests.get(BASE_URL)
    return response

def get_state(state_id):
    response = requests.get(f"{BASE_URL}/{state_id}")
    return response

def get_state_by_name(state_name):
    response = requests.get(f"{BASE_URL}/{state_name}")
    return response

def create_state(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response

def update_state(state_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{state_id}", json=data)
    return response

def delete_state(state_id):
    response = requests.delete(f"{BASE_URL}/{state_id}")
    return response

def get_objects_by_state(state_id):
    response = requests.get(f"{BASE_URL}/{state_id}/objects")
    return response

if __name__ == "__main__":
    pass