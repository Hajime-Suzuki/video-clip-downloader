import json
import subprocess
from pprint import pprint
from time import sleep
import requests
from bs4 import BeautifulSoup
import os

"""
This script generates json files from search result.
"""

search_result_url = input('search result url: ')
output_filename = input('output filename: ')


def p(item):
    pprint(item, indent='2')


def save_data(filename: str, data):
    open(filename, 'w').write(
        json.dumps(data, ensure_ascii=False))


def get_data(count: int):
    url = f'{search_result_url}&page={count}'

    res = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    video_lists = soup.find_all('li', {'class': 'video'})

    if not len(video_lists):
        return None

    title_wrappers = [l.find('a', {'class': 'title'}) for l in video_lists]
    title_and_urls = [
        {
            'title': title.get('title'),
            'url': f"https:{title.get('href')}"
        }
        for title in title_wrappers
    ]

    return title_and_urls


out_dir = f'data/{output_filename}'

if not os.path.isdir(out_dir):
    os.mkdir(out_dir)

for i in range(1, 20):
    print(i)
    data = get_data(i)

    if not data:
        break

    save_data(f'{out_dir}/{i}.json', data)

    sleep(1)
