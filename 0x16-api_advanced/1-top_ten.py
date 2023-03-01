#!/usr/bin/python3
"""
Top Ten
"""

from requests import get
import json


def top_ten(subreddit):
    """
    a function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print('None')

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = get(url, headers=user_agent, allow_redirects=False)

    try:
        results = response.json().get('data').get('children')
        for post in results:
            print(post['data']['title'])
    except Exception:
        print('None')

# if __name__ == '__main__':
#    top_ten('dankmemes')
