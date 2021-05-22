import requests
import sys
from collections import Counter

twitter_get_user_timeline_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
headers = {'Authorization': 'Bearer ' + ''}  # add token here


def get_user_timeline(name):
    resp = requests.get(twitter_get_user_timeline_url,
                 params={'screen_name': name, 'count': 200, 'include_rts': True},
                 headers=headers)
    return resp


def get_favorites(name):
    resp = requests.get('https://api.twitter.com/1.1/favorites/list.json', 
        params={'screen_name': name, 'count': 200},
        headers=headers)
    return resp


def extract_source(tweets):
    sources = Counter()
    for source in [t['source'] for t in tweets]:
        source = source[source.index('>')+1:]
        source = source[:source.index('<')]
        sources[source] += 1
    return sources


if __name__ == '__main__':
    username = sys.argv[1] if len(sys.argv) > 1 else 'netanyahu'
    timeline = get_user_timeline(username)
    print(f'Collecting Twitter sources for id {username}')
    print(f'Number of tweets fetched: {len(timeline.json())}')

    sources = extract_source(timeline.json())
    for s, c in sources.items():
        print(s, c)

