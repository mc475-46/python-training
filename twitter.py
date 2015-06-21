import requests
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session('hoge',
                        'hoge',
                        'hoge',
                        'hoge')
url = 'https://api.twitter.com/1.1/statuses/update.json'
print('tweet: ',end='')
params = {'status': input()}
r = twitter.post(url,params=params)
print(r.status_code, r.headers['content-type'])