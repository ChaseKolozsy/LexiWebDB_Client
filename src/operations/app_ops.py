import requests

BASE_URL = 'http://localhost:5002'

def initialize_database():
    response = requests.get(f'{BASE_URL}/init_db')
    if response.status_code == 200:
        print("Database initialized successfully!")
    else:
        print(f"Error initializing database: {response.json()}")

def reset_database():
    response = requests.post(f'{BASE_URL}/reset_db')
    if response.status_code == 200:
        print("Database reset and reinitialized successfully!")
    else:
        print(f"Error resetting database: {response.json()}")

def initialize_db_with_opt_in_fields(opt_in_fields=None):
    initialize_database()
    response = requests.post(f'{BASE_URL}/drop_columns', json={'opt_in_fields': opt_in_fields})
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error initializing database with opt-in fields: {response.json()}")

def reset_db_with_opt_in_fields(opt_in_fields=None):
    reset_database()
    response = requests.post(f'{BASE_URL}/drop_columns', json={'opt_in_fields': opt_in_fields})
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error initializing database with opt-in fields: {response.json()}")

if __name__ == '__main__':
    initialize_database()
    reset_database()
    opt_in_fields = ['enumerated_lemma', 'definition', 'part_of_speech', 'frequency', 'familiar']
    print(initialize_db_with_opt_in_fields(opt_in_fields))
    print(reset_db_with_opt_in_fields(opt_in_fields))

