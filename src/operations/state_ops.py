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

def get_objects_by_state(state_id):
    response = requests.get(f"{BASE_URL}/{state_id}/objects")
    return response.json()

if __name__ == "__main__":
    import app_ops
    app_ops.reset_db()

    # Example usage
    print("Schema:", get_states_schema())
    
    
    new_state = create_state("New State")
    print("\n\nCreated State:", new_state)
    print("\nAll States:", get_all_states())
    
    state_id = new_state.get("state_id")
    print("\nState ID:", state_id)

    if state_id:
        print("Get State:", get_state(state_id))
        
        updated_state = update_state(state_id, "Updated State")
        print("\n\nUpdated State:", updated_state)
        print("\nAll States:", get_all_states())
        
        print("\n\nGet State by Name:", get_state_by_name("Updated State"))

        print("\n\nDelete State:", delete_state(state_id))
        print("\nAll States:", get_all_states())
    