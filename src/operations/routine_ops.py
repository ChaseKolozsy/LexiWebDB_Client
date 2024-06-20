import requests

BASE_URL = "http://localhost:5002/api/routines"

def get_routines_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response

def get_all_routines():
    response = requests.get(BASE_URL)
    return response

def get_routine(routine_id):
    response = requests.get(f"{BASE_URL}/{routine_id}")
    return response

def get_routine_by_name(routine_name):
    response = requests.get(f"{BASE_URL}/{routine_name}")
    return response

def create_routine(name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.post(BASE_URL, json=data)
    return response

def update_routine(routine_id, name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.put(f"{BASE_URL}/{routine_id}", json=data)
    return response

def delete_routine(routine_id):
    response = requests.delete(f"{BASE_URL}/{routine_id}")
    return response

def get_objects_by_routine(routine_id):
    response = requests.get(f"{BASE_URL}/{routine_id}/objects")
    return response

if __name__ == "__main__":
    pass