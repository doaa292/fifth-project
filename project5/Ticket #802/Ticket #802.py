from flask import Flask, request

app = Flask(__name__)

@app.route("/weather")
def weather():
    # use get() instead of ["city"]
    city = request.args.get("city")
    if not city:
        return "Error: city is missing", 400
    return f"Sunny in {city}"

if __name__ == "__main__":
    app.run(debug=True)