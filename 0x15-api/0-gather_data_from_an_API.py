#!/usr/local/bin/python3
"This is a line of text"

if __name__ == "__main__":
    import requests
    import sys

    d = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(d)
    emp_json = requests.get(emp_url).json()
    t = "https://jsonplaceholder.typicode.com/todos?userId={}".format(d)
    t_json = requests.get(t).json()
    done = []
    completed = 0
    total = 0
    n = emp_json.get('name')
    for task in t_json:
        if task.get('completed') is True:
            done.append(task['title'])
            completed += 1
        total += 1
    print("Employee {} is done with tasks({}/{}:)".format(n, completed, total))
    for title in done:
        print("\t {}".format(title))
