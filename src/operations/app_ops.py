import requests

BASE_URL = 'http://localhost:5002'

def init_db():
    response = requests.get(f'{BASE_URL}/init_db')
    return response

def reset_db():
    response = requests.post(f'{BASE_URL}/reset_db')
    return response

def init_db_with_opt_in_fields(*, table_name: str, opt_in_fields: list):
    init_db()
    response = requests.post(f'{BASE_URL}/drop_columns', json={'table_name': table_name, 'opt_in_fields': opt_in_fields})
    return response

def reset_db_with_opt_in_fields(*, table_name: str, opt_in_fields: list):
    reset_db()
    response = requests.post(f'{BASE_URL}/drop_columns', json={'table_name': table_name, 'opt_in_fields': opt_in_fields})
    return response

def get_encoding():
    response = requests.get(f'{BASE_URL}/get_encoding')
    return response

def set_encoding():
    response = requests.post(f'{BASE_URL}/set_encoding')
    return response

if __name__ == '__main__':
    init_db()
    reset_db()
    get_encoding()
