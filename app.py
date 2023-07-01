from flask import Flask, request
import requests
import os

from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  

@app.route('/api/weather/get_weather_data', methods=['GET'])
def get_weather_data():
    
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    ## Define the parameters
    params = {
        'lat': lat,
        'lon': lng,
        'appid': os.getenv("OPENWEATHERAPIKEY")
         }

    ## Send GET request
    response = requests.get(base_url, params=params)

    ## Convert the response to JSON
    weather_data = response.json()

    return jsonify(weather_data)


if __name__ == '__main__':
    app.run(debug=True)