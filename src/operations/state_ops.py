import requests

BASE_URL = "http://localhost:5002/states"

def get_states_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_states():
    response = requests.get(BASE_URL)
    return response.json()

def get_state(state_id):
    response = requests.get(f"{BASE_URL}/{state_id}")
    return response.json()

def get_state_by_name(state_name):
    response = requests.get(f"{BASE_URL}/{state_name}")
    return response.json()

def create_state(name):
    data = {"name": name}
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_state(state_id, name):
    data = {"name": name}
    response = requests.put(f"{BASE_URL}/{state_id}", json=data)
    return response.json()

def delete_state(state_id):
    response = requests.delete(f"{BASE_URL}/{state_id}")
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Schema:", get_states_schema())
    
    print("All States:", get_all_states())
    
    new_state = create_state("New State")
    print("Created State:", new_state)
    
    state_id = new_state.get("id")
    if state_id:
        print("Get State:", get_state(state_id))
        
        updated_state = update_state(state_id, "Updated State")
        print("Updated State:", updated_state)
        
        print("Delete State:", delete_state(state_id))
    
    print("Get State by Name:", get_state_by_name("Updated State"))