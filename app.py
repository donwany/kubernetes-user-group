import datetime
from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Machine Learning API!"


@app.route("/fraud")
def fraud():
    return jsonify(
        {
            "FraudProbability": 0.90,
            "NotFraudProbability": 0.10,
            "Datetime": datetime.datetime.now(),
            "ModelType": "RandomForest",
        }
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=23321)
