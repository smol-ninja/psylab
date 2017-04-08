import requests
import json

BASE_URL = 'http://nimblerest.lisuns.com:4531/'
ACCESS_KEY = '6e9ae175-e8a2-4b8b-9ba8-113ca81a9788'

def parse_params(name, **kwargs):
    suburl = 'accessKey=%s&xml=false&' % (ACCESS_KEY, )
    for key in kwargs:
        suburl += "%s=%s&" % (key, kwargs[key])
    return BASE_URL + name + '/?' + suburl

url = parse_params(name='GetSnapshot', exchange='NSE', instrumentIdentifiers='icicibank+sbin+acc')
response = requests.get(url)
try:
    print json.loads(response.text)
except:
    print response.text
