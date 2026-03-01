import requests

url = 'http://localhost:5678/webhook-test/1d4206d8-ff1b-49fa-8eda-9812ef572734'

#message given to the ai
user_message  ='how are you?'

request_message = {'message':user_message}

#the message is directed to the ai agent via the specific url
response = requests.post(url,json=request_message)

#printing the status of input given to ai
print(response.status_code)

#printing the ai response.
print(response.json()[0]['output'])

