from flask import Flask

from flask import jsonify
from flask_cors import CORS
from weather import weather


app = Flask(__name__)

app.register_blueprint(weather)


if __name__ == '__main__':
    app.run(debug=True)