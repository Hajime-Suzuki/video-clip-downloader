import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from time import sleep
import subprocess


def p(item):
    pprint(item, indent='2')


def save_data(filename: str, data):
    open(filename, 'w').write(
        json.dumps(data, ensure_ascii=False))


def get_data(count: int):
    url = f'https://search.bilibili.com/all?keyword=%E8%A3%95%E9%9D%99%E7%9A%84%E4%BA%92%E4%B8%8D%E7%9B%B8%E8%AE%A9%E5%B9%BF%E6%92%AD&order=pubdate&duration=0&tids_1=0&page={count}'

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


for i in range(1, 20):
    print(i)
    data = get_data(i)

    if not data:
        break

    save_data(f'data/yuzuradi-{i}.json', data)

    for d in data:
        subprocess.run(['you-get', '--format=flv360', d['url']])

    sleep(1)
