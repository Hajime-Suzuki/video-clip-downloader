import requests

res = requests.get('https://pwa-test-1234.netlify.com/')

with open('test.html', 'w') as file:
    file.write(res.text)
    print(res.headers)
