import requests
'''
Queries the Reddit API and prints titles of the first 10 top
posts for subreddit.
'''


def top_ten(subreddit):
    '''
    Queries the Reddit API and prints the titles of the first 10 hot posts for
    a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    None
    '''
    # Construct the URL for the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set the User-Agent header to identify ourselves to the Reddit API
    headers = {
            "User-Agent": "MyRedditApp/1.0 (by LawsonLawson, Github:https://\
                                            github.com/LawsonLawson)"
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the list of posts from the response
        posts = data["data"]["children"]

        # Iterate over the posts and print their titles
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        # Print "None" if the subreddit is not valid or the request failed
        print("None")
