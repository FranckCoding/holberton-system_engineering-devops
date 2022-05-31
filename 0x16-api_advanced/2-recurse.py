#!/usr/bin/python3
"""
Task 2
"""

import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """
    if after is None:
        return

    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            headers={'User-agent': 'Wololo'},
                            params={'after': after})
    if response is None or response.status_code != 200:
        return None

    data = response.json()['data']
    for article in data['children']:
        hot_list.append(article)
    recurse(subreddit, hot_list, data['after'])

    return hot_list
