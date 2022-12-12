import requests

TOKEN = ""
USERNAME = ""

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph-1",
    "name": "Programing Graph",
    "unit": "Lines",
    "type": "float",
    "color": "kuro",
    "timezone": "Poland",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
