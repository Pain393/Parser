import requests
import json
from pprint import pprint


def get_data(url):
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            break
    return response.json()


username = 'pain393'
url = f'https://api.github.com/users/{username}/repos'

response = get_data(url)
# pprint(response)

rep = []
for item in response:
    rep.append(item['name'])
print(f'\nРепозитории пользователя {username}:\n{rep}')

with open('1_1.json', 'w') as f:
    json.dump(rep, f)
