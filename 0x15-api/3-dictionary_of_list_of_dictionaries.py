#!/usr/bin/python3
'''
Records all tasks that are owned by this employee
'''


import json
import requests

url = "https://jsonplaceholder.typicode.com/users"


def create_dictionnary(users):
    '''
    create a dictionnary with the api request
    '''
    dictionnary = {}
    for user in users.json():
        user_tasks = requests.get("{}/{}/todos".format(
            url, user['id'])).json()
        if user_tasks:
            dictionnary[str(user['id'])] = []
            for value in user_tasks:
                dictionnary[str(user['id'])].append(
                    {"username": user["username"],
                     "task": value['title'],
                     "completed": value['completed']}
                    )

    return dictionnary


def main():
    '''
    main function that not be executable if not main
    '''
    users = requests.get("{}".format(url))

    if users:
        dictionnary = create_dictionnary(users)

        json_object = json.dumps(dictionnary)

        with open('todo_all_employees.json', mode='w') as json_file:
            json_file.write(json_object)


if __name__ == '__main__':
    main()
