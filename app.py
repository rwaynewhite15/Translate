from gettext import translation
import requests, uuid, json

# Add your subscription key and endpoint
subscription_key = "4b2b03351cd74b12a767c1331b9fc3b0"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "global"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['es', 'it']
}

constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'My name is Bobby, I hope you have a wonderful day!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
output = json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))
print(output)
output_file = open('output.json', 'w')
output_file.write(output)