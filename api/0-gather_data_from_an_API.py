import requests

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/1')
    employee = employee_response.json()

    # Fetch employee's TODOs
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/users/1/todos')
    todos = todos_response.json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    
    # Display the progress
    print(f'Employee {employee["name"]} is done with tasks({done_tasks}/{total_tasks}):')
    
    # Display the titles of completed tasks
    for todo in todos:
        if todo['completed']:
            print('\t ' + todo['title'])

# Test the function with an example employee ID
get_employee_todo_progress(1)
