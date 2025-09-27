import os
import requests
from flask import Flask
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

def get_data(city):
    return requests.get(f"https://api.example.com/{city}?key={API_KEY}").json()

@app.route("/weather")
def weather():
    return get_data("Amman")

if __name__ == "__main__":
    app.run(debug=True)