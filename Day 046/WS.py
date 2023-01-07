
import json

with open("token.txt", encoding="utf8") as file:
    content = json.load(file)
    # content = file.read()
    access_token = content["access_token"]
    print(access_token)