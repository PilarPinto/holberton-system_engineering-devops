#!/usr/bin/python3
'''
Gathering the top ten reddit
programming posts (hot)
'''
import requests


def top_ten(subreddit):

    sub_url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    reddit_sub = requests.get(sub_url, allow_redirects=False,
                              headers={'User-Agent': 'My User Agent 1.0'})
    if reddit_sub:
        re2j = reddit_sub.json()
        access_data = re2j.get('data').get('children')

        data_lst = []

        for ind in access_data[:10]:
            data_lst.append(ind.get('data').get('title'))

        for i in data_lst:
            print(i)
    else:
        print('None')
