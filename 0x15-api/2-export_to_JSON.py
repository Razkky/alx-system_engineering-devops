#!/usr/bin/python3
"""Use the Rest api to get employee todo list
    and export all completed todo to csv file
"""
import json
import csv
import os
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    id = sys.argv[1]
    user = requests.get(url + "users/{}".format(id)).json()
    todos = requests.get(url + "todos", params={"userId": id}).json()
    file = id + ".json"
    with open(file, 'w', newline='') as file:
        json.dump({id: [{"task": todo.get('title'),
                        "completed": todo.get("completed"),
                         "username": user.get('name')}
                        for todo in todos]}, file)
