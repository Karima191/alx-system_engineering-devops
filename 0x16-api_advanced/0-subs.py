#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0

        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        data = response.json().get("data")
        if data is None:
            return 0

        return data.get("subscribers", 0)  # Return 0 if "subscribers" is not found

    except requests.exceptions.HTTPError as http_err:
        return 0
    except requests.exceptions.RequestException as req_err:
        return 0
    except ValueError as json_err:
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
    else:
        print("Please pass an argument for the subreddit to search.")
