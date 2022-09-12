#!/usr/bin/python3
"This is a line of text"

if __name__ == "__main__":
    import json
    import requests

    emp_url = "https://jsonplaceholder.typicode.com/users"
    emp_json = requests.get(emp_url).json()
    t = "https://jsonplaceholder.typicode.com/todos"
    t_json = requests.get(t).json()
    all_emp = {}
    for emp in emp_json:
        tasks = []
        for task in t_json:
            if task.get('userId') == emp.get('id'):
                tasks.append({'username': emp.get('username'),
                              'task': task.get('title'),
                              'completed': task.get('completed')})
        all_emp[emp.get('id')] = tasks
    with open("todo_all_employees.json", 'w') as new_file:
        json.dump(all_emp, new_file)
