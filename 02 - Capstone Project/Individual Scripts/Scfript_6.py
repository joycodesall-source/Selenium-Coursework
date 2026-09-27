import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data):
        return requests.post(
            self.base_url + endpoint,
            data=data
        )

def verify_login(client, email, password):
    endpoint = "/api/verifyLogin"

    data = {
        "email": email,
        "password": password
    }
    return client.post(endpoint, data)

BASE_URL = "https://automationexercise.com"
EMAIL = "joycodesall@gmail.com"
PASSWORD = "Excellent@233"

client = APIClient(BASE_URL)

response = verify_login(client, EMAIL, PASSWORD)

print("Status Code:", response.status_code)
print("Response:", response.json())

assert response.status_code == 200
assert response.json()["responseCode"] == 200
assert response.json()["message"] == "User exists!"