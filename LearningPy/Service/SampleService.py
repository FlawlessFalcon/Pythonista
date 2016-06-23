'''
 How to get started with Requests

'''

__author__="Ganesh"

import requests, json

resJson = requests.get('https://api.github.com/events')
if(resJson.ok):
    resp = resJson.json()
    resp1 = json.loads(resJson.content)

print json.dumps(resp1, indent=4, sort_keys=True)


def consumeGETRequestSync():
    data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
    headers = {"Accept": "application/json"}
 # call get service with headers and params
    response = requests.get(url,data = data)
    print "code:"+ str(response.status_code)
    print "******************"
    print "headers:"+ str(response.headers)
    print "******************"
    print "content:"+ str(response.text)

print consumeGETRequestSync()