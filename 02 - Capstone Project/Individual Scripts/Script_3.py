import requests

url = "https://automationexercise.com/api/verifyLogin"

data = {
    "email": "joycodesall@gmail.com",
    "password": "Excellent@233"
}

response = requests.post(url, data=data)

print("Status Code:", response.status_code)
print("Response:", response.json())

assert response.status_code == 200
assert response.json()["message"] == "User exists!"