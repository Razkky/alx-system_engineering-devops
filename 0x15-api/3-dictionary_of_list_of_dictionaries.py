#!/usr/bin/python3
"""Use the Rest api to get employee todo list
    and export all completed todo to csv file
"""
import csv
import json
import os
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()
    file = "odo_all_employees.json"
    with open(file, 'w') as file:
        for user in users:
            todos = requests.get(
                    url + "todos", params={"userId": user.get('id')}).json()
            json.dump({user.get('id'): [{"username": user.get('name'),
                                        "task": todo.get('title'),
                                         "completed": todo.get("completed")}
                                        for todo in todos]}, file)
