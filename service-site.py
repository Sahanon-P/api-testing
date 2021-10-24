import unittest
import requests
import datetime
URL = "https://suchonsite-server.herokuapp.com/"
    

class TestAPI(unittest.TestCase):
    def setUp(self):
        pass

    #This test might not necessary but it's a part of the API
    def test_get_all_people(self):
        endpoint = URL + "people/all"
        response = requests.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertEqual("application/json; charset=utf-8", response.headers["Content-Type"])

    def test_get_today_appoinment(self):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        endpoint = URL + f"people/by_date/{today}"
        response = requests.get(endpoint)
        # Today not have any appointment
        self.assertEqual(response.text, "")

    def test_get_appoinment_by_date(self):
        # Only this date that provide the data
        endpoint = URL + f"people/by_date/20-10-2021"
        response = requests.get(endpoint)
        self.assertEqual("application/json; charset=utf-8", response.headers["Content-Type"])

    def test_get_appointment_with_unexisting_date(self):
        endpoint = URL + f"people/by_date/20-20-2021"
        response = requests.get(endpoint)
        self.assertEqual(404, response.status_code)

    def test_get_appointment_without_date(self):
        endpoint = URL + f"people/by_date/"
        response = requests.get(endpoint)
        self.assertEqual(404, response.status_code)

    def test_get_appointment_with_invalid_date(self):
        endpoint = URL + f"people/by_date/twenty-oct-2021"
        response = requests.get(endpoint)
        self.assertEqual(404, response.status_code)

    def test_date_with_parse_date(self):
        endpoint = URL + f"people/by_date/20-10-2021"
        response = requests.get(endpoint)
        date = response.json()['date']
        self.assertEqual(date, "20-10-2021")




if __name__ == '__main__':
    unittest.main()