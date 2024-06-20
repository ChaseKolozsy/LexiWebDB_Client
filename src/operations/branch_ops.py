import requests

BASE_URL = 'http://localhost:5002/api/branches'

def get_branches_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response

def create_branch(root_node, branch_name):
    data = {
        'root_node': root_node,
        'branch_name': branch_name
    }
    response = requests.post(BASE_URL, json=data)
    return response

def get_all_branches():
    response = requests.get(BASE_URL)
    return response

def get_branch_by_id(branch_id):
    response = requests.get(f'{BASE_URL}/{branch_id}')
    return response

def update_branch(branch_id, data):
    response = requests.put(f'{BASE_URL}/{branch_id}', json=data)
    return response

def delete_branch(branch_id):
    response = requests.delete(f'{BASE_URL}/{branch_id}')
    return response

if __name__ == '__main__':
    pass