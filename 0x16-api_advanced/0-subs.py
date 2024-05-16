#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced:v1.0.0 (by /u/efaeleng)'}

    try:
        response = requests.get(url, headers=headers)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print("Error:", response.status_code)
            print("Response Content:", response.content.decode())
            return 0  # Invalid subreddit or other error occurred

    except requests.RequestException as e:
        print("Request Exception:", e)
        return 0  # Request failed or network error
