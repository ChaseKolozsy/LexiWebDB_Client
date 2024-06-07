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

if __name__ == '__main__':
    print(initialize_database())
    print(reset_database())

