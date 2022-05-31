#!/usr/bin/python3
"""
Task 1
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            headers={'User-agent': 'Wololo'})
    if response is None or response.status_code != 200:
        print('None')
    else:
        data = response.json()['data']['children']
        for loop in range(0, 10):
            print(data[loop]['data']['title'])
