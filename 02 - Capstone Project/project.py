import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(self.base_url + endpoint)

    def post(self, endpoint, data=None):
        return requests.post(
            self.base_url + endpoint,
            data=data
        )

BASE_URL = "https://automationexercise.com"
EMAIL = "joycodesall@gmail.com"
PASSWORD = "Excellent@233"
client = APIClient(BASE_URL)