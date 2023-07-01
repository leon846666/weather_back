import unittest
import json

from app import app


class TestMyModule(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_data(self):
        response = self.app.get('/api/weather/get_weather_data?lat=5&lng=22')
        print(response)
        jsonData = json.loads(response.data)
        print("jsonData",jsonData)
        self.assertEqual(jsonData['cod'], 200)


if __name__ == '__main__':
    unittest.main()