import requests

print('Search Word: ',end='')
word = input()
r = requests.get('http://connpass.com/api/v1/event/?keyword='+word)
print(r.status_code, r.headers['content-type'])

for event in r.json()['events'][:10]:
    print(event['title'], event['started_at'])