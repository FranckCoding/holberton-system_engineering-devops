#!/usr/bin/python3
"""
Task 0 - Use Reddit API with Python
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0
    """
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={'User-agent': 'Wololo'})
    if response is None or response.status_code != 200:
        return 0

    response_data = response.json()['data']

    return response_data['subscribers']
