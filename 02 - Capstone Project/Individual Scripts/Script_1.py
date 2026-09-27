import requests

# JSONPlaceholder User API
url = "https://jsonplaceholder.typicode.com/users/1"

# Sends GET request
response = requests.get(url)

# Displays response
print("Status Code:", response.status_code)
print("User Details:", response.json())

# Validates successful response
assert response.status_code == 200