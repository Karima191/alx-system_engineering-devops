#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers (total subscribers) for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "YourCustomUserAgent"}  # Set your custom User-Agent here
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

# Example usage:
subreddit_name = "learnpython"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers on r/{subreddit_name}: {subscribers_count}")

