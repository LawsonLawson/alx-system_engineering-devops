#!/usr/bin/python3
'''
This function queries the number of subscribers on a given Reddit subreddit.
'''


import requests


def number_of_subscribers(subreddit):
    '''
    Returns the total number of subscribers on a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The total number of subscribers on the subreddit.
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "MyRedditApp/1.0 (by LawsonLawson, Github:https://\
                                            github.com/LawsonLawson)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
