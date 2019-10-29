import requests
import json
from sqlscripts.parsediscordconfigs import url
webhookurl = url

def execute_webhook(content):
	data = {}
	data["content"] = content
	data["username"] = "coybot"
	result = requests.post(webhookurl, data=json.dumps(data), headers={"Content-Type": "application/json"})
	try:
	    result.raise_for_status()
	except requests.exceptions.HTTPError as err:
	    print(err)
	else:
	    print("Payload delivered successfully, code {}.".format(result.status_code))
