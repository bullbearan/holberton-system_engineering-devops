#!/usr/bin/python3
"This is a line of text"

if __name__ == "__main__":
    import json
    import requests
    import sys

    d = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(d)
    emp_json = requests.get(emp_url).json()
    t = "https://jsonplaceholder.typicode.com/users/{}/todos".format(d)
    t_json = requests.get(t).json()
    name = emp_json.get("username")
    tasks = []
    for task in t_json:
        tasks.append({'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': name})
    with open("{}.json".format(d), 'w') as new_file:
        json.dump({"{}".format(d): tasks}, new_file)
