#!/usr/bin/python3
'''
Records all tasks that are owned by this employee
'''


import requests
from sys import argv
import json

url = "https://jsonplaceholder.typicode.com/users"


def main():
    '''
    main function that not be executable if not main
    '''
    user = requests.get("{}/{}".format(url, argv[1])).json()
    user_tasks = requests.get("{}/{}/todos".format(url, argv[1])).json()

    if user and user_tasks:
        dictionnary = {str(argv[1]): []}
        for value in user_tasks:
            dictionnary[str(argv[1])].append({"task": value['title'],
                                              "completed": value['completed'],
                                              "username": user["username"]})

        json_object = json.dumps(dictionnary)

        with open('{}.json'.format(argv[1]), mode='w') as json_file:
            json_file.write(json_object)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1].isdigit():
        main()
