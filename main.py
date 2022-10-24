import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(f"hello world: {r.status_code}")
