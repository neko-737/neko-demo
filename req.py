# backend.py
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        # wttr.in provides weather info without API key
        url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
