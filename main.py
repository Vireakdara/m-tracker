import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
user_name = "vireakdara"
token = "000261815"
id = "graph1"
now = dt.datetime.now().strftime('%Y%m%d')

user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_params = {
    "id": id,
    "name": "Coding",
    "unit": "time",
    "type": "int",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)
post_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{id}"

post_params = {
    # date format yyyymmdd
    "date": now,
    "quantity": '1',
}

response = requests.post(url=post_endpoint, json=post_params, headers=header)
print(response.text)
