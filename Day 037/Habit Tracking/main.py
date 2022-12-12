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
    "id": "graph-2",
    "name": "Programing Graph",
    "unit": "contributions",
    "type": "int",
    "color": "kuro",
    "timezone": "Poland",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_config['id']}"

pixel_data = {
    "date": "20221211",
    "quantity": "1",
    # "optionalData": "",
}

response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)