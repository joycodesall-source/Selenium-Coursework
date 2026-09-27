import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("User ID:", response.json()["id"])
print("Name:", response.json()["name"])
print("Username:", response.json()["username"])
print("Email:", response.json()["email"])

assert response.status_code == 200
assert response.json()["id"] == 1