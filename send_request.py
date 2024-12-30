import requests

url = "http://localhost:8000/items/"
headers = {
    "host": "example.com",
    "save_data": "true",  # booleans should be passed as strings ('true' or 'false')
    "if_modified_since": "Wed, 21 Oct 2023 07:28:00 GMT",
    "traceparent": "00-fd69e57c1b83304b83140686eea28c4a-4cc98f62d63a505d-01",
    "x_tags": "tag1, tag2, tag3",  # Comma-separated list
}

response = requests.get(url, headers=headers)
print(response.json())



