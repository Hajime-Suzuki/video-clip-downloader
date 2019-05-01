import requests

res = requests.get('https://realpython.com/python-requests/')

with open('test.html', 'w') as file:
    file.write(res.text)
