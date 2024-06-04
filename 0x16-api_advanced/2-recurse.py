#!/usr/bin/python3
'''
This script returns a list containing the titles of all hot articles for a
given subreddit. If the subreddit is invalid, the function returns None.
It uses a recursive approach.
'''

import requests


def recurse(subreddit, hot_list=[], after=None):
    ''''
    Retrieves a list of titles of all hot articles for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): A list to store the titles of hot articles.
    after (str): The identifier for the next page of results.

    Returns:
    list: A list containing the titles of all hot articles for a given
    subreddit. If the subreddit is invalid, the function returns None.
    '''
    # Base URL for Reddit API with the subreddit and 'hot' endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditApp/1.0 (by LawsonLawson, Github:https://\
                                            github.com/LawsonLawson)"
    }
    params = {'after': after, 'limit': 100} if after else {'limit': 100}

    # Making the request to Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json().get('data', {})
    if not data:
        return None

    # Extracting the list of hot articles and pagination token
    children = data.get('children', [])
    after = data.get('after')

    # Accumulate the titles of hot articles
    for child in children:
        hot_list.append(child.get('data', {}).get('title'))

    # If there is a next page, recursively fetch the next set of hot articles
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
