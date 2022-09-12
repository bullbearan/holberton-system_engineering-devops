#!/usr/bin/python3
"This is a line of text"

if __name__ == "__main__":
    import csv
    import requests
    import sys

    d = sys.argv[1]
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(d)
    emp_json = requests.get(emp_url).json()
    t = "https://jsonplaceholder.typicode.com/users/{}/todos".format(d)
    t_json = requests.get(t).json()
    name = emp_json.get("username")
    with open("{}.csv".format(d), 'w') as new_file:
        writer = csv.writer(new_file, quoting=csv.QUOTE_ALL)
        for ta in t_json:
            writer.writerow([d, name, ta.get('completed'), ta.get('title')])
