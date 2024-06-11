import requests

BASE_URL = "http://localhost:5002/routines"

def get_routines_schema():
    response = requests.get(f"{BASE_URL}/schema")
    return response.json()

def get_all_routines():
    response = requests.get(BASE_URL)
    return response.json()

def get_routine(routine_id):
    response = requests.get(f"{BASE_URL}/{routine_id}")
    return response.json()

def get_routine_by_name(routine_name):
    response = requests.get(f"{BASE_URL}/{routine_name}")
    return response.json()

def create_routine(name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def update_routine(routine_id, name, description):
    data = {
        "name": name,
        "description": description
    }
    response = requests.put(f"{BASE_URL}/{routine_id}", json=data)
    return response.json()

def delete_routine(routine_id):
    response = requests.delete(f"{BASE_URL}/{routine_id}")
    return response.json()

if __name__ == "__main__":
    # Example usage
    print("Schema:", get_routines_schema())
    
    print("All Routines:", get_all_routines())
    
    new_routine = create_routine("Morning Routine", "Wake up, exercise, breakfast")
    print("Created Routine:", new_routine)
    
    routine_id = new_routine.get("id")
    if routine_id:
        print("Get Routine:", get_routine(routine_id))
        
        updated_routine = update_routine(routine_id, "Updated Morning Routine", "Wake up, exercise, breakfast, read")
        print("Updated Routine:", updated_routine)
        
        print("Delete Routine:", delete_routine(routine_id))
    
    print("Get Routine by Name:", get_routine_by_name("Updated Morning Routine"))