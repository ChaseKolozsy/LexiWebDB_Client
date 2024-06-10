import requests

BASE_URL = 'http://localhost:5002/branches'

def get_branches_schema():
    response = requests.get(f'{BASE_URL}/schema')
    return response.json()

def create_branch(root_node, branch_name):
    data = {
        'root_node': root_node,
        'branch_name': branch_name
    }
    response = requests.post(BASE_URL, json=data)
    return response.json()

def get_all_branches():
    response = requests.get(BASE_URL)
    return response.json()

def get_branch_by_id(branch_id):
    response = requests.get(f'{BASE_URL}/{branch_id}')
    return response.json()

def update_branch(branch_id, data):
    response = requests.put(f'{BASE_URL}/{branch_id}', json=data)
    return response.json()

def delete_branch(branch_id):
    response = requests.delete(f'{BASE_URL}/{branch_id}')
    return response.json()

if __name__ == '__main__':
    import app_ops
    # Example usage
    app_ops.reset_db()

    print("Schema:", get_branches_schema())

    print("\n\nCreating branch:", create_branch('root1', 'branch1'))
    print("All branches:", get_all_branches())

    branch_id = 1
    print(f"\n\nBranch {branch_id}:", get_branch_by_id(branch_id))

    update_data = {'branch_name': 'updated_branch1'}
    print(f"\n\nUpdating branch {branch_id}:", update_branch(branch_id, update_data))
    print(f"Branch {branch_id}:", get_branch_by_id(branch_id))

    print(f"\n\nDeleting branch {branch_id}:", delete_branch(branch_id))
    print("All branches:", get_all_branches())

