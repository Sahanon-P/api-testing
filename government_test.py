import unittest
import requests


URL = "https://wcg-apis.herokuapp.com/"
class TestGovernment(unittest.TestCase):
    sample_data = [
        {
            "citizen_id":"1111111111111",
            "name":"Steve",
            "surname":"Guy", 
            "birth_date": "08-08-2008",
            "occupation":"Human",
            "address":"Home",
        },
        {
            "citizen_id":"2222222222222",
            "name":"Mark",
            "surname":"Guy", 
            "birth_date": "07-07-2007",
            "occupation":"Human",
            "address":"Home",
        }
    ]
    def setUp(self):
        for p in self.sample_data: 
            endpoint = URL + f"registration?citizen_id={p['citizen_id']}&name={p['name']}&surname={['surname']}&birth_date={p['birth_date']}&occupation={p['occupation']}&address={p['address']}"
            response = requests.post(endpoint)
            print(response.json()['feedback'])

    def test_get_all_people(self):
        endpoint = URL + f"registration"
        response = requests.get(endpoint)
        data = response.json()
        self.assertEqual("1111111111111",data[0]['citizen_id'])
        self.assertEqual("2222222222222",data[1]['citizen_id']) 

    def tearDown(self):
        endpoint = URL + f"citizen"
        response = requests.delete(endpoint)


if __name__ == "__main__":
    unittest.main()
        
            
        