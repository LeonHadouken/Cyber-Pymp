import requests
import json
import time

def StartDay(moment,):
    url = "https://api.airtable.com/v0/appklLhkULpc5qp0P/Fact%20Schedule"
    payload = "{\n  \"fields\": {\n    \"Time started\": \"now\",\n    \"Projected Time started\": \"now\",\n    \"Team member\": [\n      \"recKfwk1BhmZbXOmK\"\n    ],\n    \"Status\": \"WORKING\",\n    \"Models\": [\n      \"model_id\"\n    ]\n  }\n}'"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer keywI9ioEZH0fcJKz'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
