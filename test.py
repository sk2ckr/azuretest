import requests
r = requests.get('http://114.207.230.43')

print(r.status_code)
print(r.url)

