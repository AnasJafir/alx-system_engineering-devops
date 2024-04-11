#!/usr/bin/python3
"""Subscribers API Module"""
import requests


def number_of_subscribers(subreddit):
    """Method that return the number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
