from flask import Flask, request

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city", "")
    if not city.isalpha():  # only letters allowed
        return "Error: invalid city name", 400
    return f"Sunny in {city}"

if __name__ == "__main__":
    app.run(debug=True)