#!/usr/bin/python3
'''
for a given employee ID, returns information about his/her TODO list progress.
'''


import requests
from sys import argv

url = "https://jsonplaceholder.typicode.com/users"


def print_api_content(username, user_tasks_done, user_tasks):
    '''
    print the api content get previously
    '''
    print("Employee {} is done with tasks({}/{}):".format(
        username["name"], len(user_tasks_done), len(user_tasks)))
    for value in user_tasks_done:
        print("\t {}".format(value["title"]))


def main():
    '''
    main function that not be executable if not main
    '''
    username = requests.get("{}/{}".format(url, argv[1])).json()
    user_tasks = requests.get("{}/{}/todos".format(url, argv[1])).json()

    if username and user_tasks:
        user_tasks_done = []
        for value in user_tasks:
            if value["completed"]:
                user_tasks_done.append(value)

        print_api_content(username, user_tasks_done, user_tasks)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        main()
