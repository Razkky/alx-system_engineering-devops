#!/usr/bin/python3
"""Use the Rest api to get employee todo list
    and export all completed todo to csv file
"""
import sys
import csv
import requests
import os


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    id = sys.argv[1]
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()
    file = id + ".csv"
    with open(file, 'w', newline='') as file:
        copy = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            copy.writerow(
                [id, user.get('name'),
                    todo.get('completed'),
                    todo.get('title')])
