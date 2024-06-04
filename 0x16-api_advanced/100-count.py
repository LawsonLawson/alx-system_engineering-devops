#!/usr/bin/python3
'''
This function recursively fetches hot article titles from a given subreddit.
'''
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    '''
    Recursively fetches hot article titles from a given subreddit and counts
    occurrences of given keywords (case-insensitive).

    Args:
    subreddit (str): The name of the subreddit.
    word_list (list): List of keywords to count.
    after (str): The identifier for the next page of results (default is None).
    counts (dict): Dictionary to store keyword counts (default is None).

    Returns:
    None: Prints the sorted counts of keywords.
    '''
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    # Define the base URL for the Reddit API with the 'hot' endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditApp/1.0 (by LawsonLawson, Github:https://\
                                            github.com/LawsonLawson)"
    }
    params = {'after': after, 'limit': 100}

    # Making the request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return

    # Parse the JSON response
    data = response.json().get('data', {})
    if not data:
        return

    # Extracting the list of hot articles and the pagination token
    children = data.get('children', [])
    after = data.get('after')

    # Count occurrences of keywords in article titles
    for child in children:
        title = child.get('data', {}).get('title', '').lower().split()
        for word in title:
            if word in counts:
                counts[word] += 1

    # If there is a next page, recursively fetch the next set of hot articles
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        # Once all pages have been fetched, print the results
        sorted_counts = sorted(counts.items(), key=lambda item:
                               (-item[1], item[0]))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
