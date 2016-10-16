import sys
import requests
import json

url = 'https://hooks.slack.com/services/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'

data = {}
data['channel'] = '#random'
data['username'] = 'webhookbot'
embedded_link = "<http://tonywillenberg.com|"+str(sys.argv[1]) + ">"
data['text'] = embedded_link
data['icon_emoji'] = ':ghost'

payload = json.dumps(data)

# GET
# r = requests.get(url)

# GET with params in URL
# r = requests.get(url, params=payload)

# POST with form-encoded data
# r = requests.post(url, data=payload)

# POST with JSON
r = requests.post(url, payload)

# Response, status etc
r.text
r.status_code