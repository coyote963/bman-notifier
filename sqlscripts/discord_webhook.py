import requests
import json
webhookurl = 'https://discordapp.com/api/webhooks/637851459203104779/AlmKXxfwx7YtAXn4cbOftRvm0I81v5rT8bF66JBHQeqQjZkmUDfrqJZau5FUYPSZbtDu'

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
