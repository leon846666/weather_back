from flask import Flask

from flask import jsonify
from flask_cors import CORS
from weather import weather
import unittest


app = Flask(__name__)

app.register_blueprint(weather)


class TestMyModule(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_data(self):
        response = self.app.get('/api/weather/get_weather_data?lat=5&lng=22')
        self.assertEqual(response.data, b'25')


if __name__ == '__main__':
    app.run(debug=True)