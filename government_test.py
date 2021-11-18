import unittest
import requests
from decouple import config

reservation_id = None
URL = "https://flamxby.herokuapp.com"
class TestGovernment(unittest.TestCase):
    def setUp(self):
        self.user_token = config('TOKEN')
        self.citizen_id = config('CITIZEN_ID')
        self.password = config('PASSWORD')

    def test_get_people_by_id(self):
        endpoint = URL+ f"/user/{self.citizen_id}"
        response = requests.get(endpoint)
        data = response.json()
        name = data['name']
        self.assertEqual("Harry", name)

    def test_get_reservation_by_id(self):
        endpoint = URL+ f"/reservation/7"
        response = requests.get(endpoint)
        data = response.json()
        vaccinate_status = data['vaccinated']
        self.assertFalse(vaccinate_status)

    def test_login(self):
        endpoint = URL + "/login"
        body = {
            "username": self.citizen_id,
            "password":self.password
        }
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        response = requests.post(endpoint, data = body, headers=headers)
        data = response.json()
        token_type = data['token_type']
        self.assertEqual("bearer", token_type)
        self.assertEqual(200, response.status_code)


    def test_reservation(self):
        endpoint_login = URL + "/login"
        body = {
            "username": self.citizen_id,
            "password": self.password
        }
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        fetch = requests.post(endpoint_login, data = body, headers=headers)
        data = fetch.json()
        token = data['access_token']
        endpoint = URL + "/reservation"
        response = requests.post(endpoint,headers={"Authorization": "Bearer " + token})
        self.assertEqual(201, response.status_code)
        



if __name__ == "__main__":
    unittest.main()