#!/usr/bin/python3
"""Subscribers API Module"""
import requests


def number_of_subscribers(subreddit):
    """Method that return the number of subs"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
